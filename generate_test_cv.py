# -*- coding: utf-8 -*-
"""
generate_test_cv.py  (v2)
--------------------------
Diagnoses the job description tokenization problem and generates
the best possible resume given the actual keywords the system extracts.

Run:  venv\Scripts\python generate_test_cv.py
"""

import sys, re, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))

import nltk
nltk.download("punkt",     quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("wordnet",   quiet=True)
nltk.download("omw-1.4",   quiet=True)

from nltk.tokenize import word_tokenize
from mysite.text_process import normalize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# ─────────────────────────────────────────────────────────────────────
# STEP 1 -- Reproduce exactly what screen.res() does to the job desc
# ─────────────────────────────────────────────────────────────────────
JOB_DETAILS          = "WRITE CLEAN CODE"
JOB_RESPONSIBILITIES = "MANAGE DEVS"
JOB_EXPERIENCE       = "1-2"

# This is the EXACT same line from screen.py line 441-442
job_desc_raw = JOB_DETAILS + "\n" + JOB_RESPONSIBILITIES + "\n" + JOB_EXPERIENCE + "\n"
job_desc_clean = re.sub(r" +", " ", job_desc_raw.replace("\n", "").replace("\r", ""))

job_tokens   = word_tokenize(str(job_desc_clean))
job_keywords = normalize(job_tokens)
job_text     = " ".join(job_keywords)

print("=" * 65)
print("STEP 1 -- Job Description Analysis (what the system ACTUALLY sees)")
print("=" * 65)
print(f"  Stored in DB    : details='{JOB_DETAILS}'")
print(f"                    responsibilities='{JOB_RESPONSIBILITIES}'")
print(f"                    experience='{JOB_EXPERIENCE}'")
print()
print(f"  After joining   : '{job_desc_clean}'")
print(f"    *** PROBLEM: newlines removed BEFORE tokenizing ***")
print(f"    'CODE' + 'MANAGE' became 'CODEMANAGE' (one merged word!)")
print()
print(f"  Tokens          : {job_tokens}")
print(f"  After normalize : {job_keywords}")
print(f"  Final job text  : '{job_text}'")
print()
print(f"  CONCLUSION: Only {len(job_keywords)} usable stem(s) in the job description.")
print(f"  A very short job desc = very hard to score well against!")
print()

# ─────────────────────────────────────────────────────────────────────
# STEP 2 -- What stems does the resume need to contain?
# ─────────────────────────────────────────────────────────────────────
print("=" * 65)
print("STEP 2 -- What keywords must the resume contain?")
print("=" * 65)

# Map each normalized stem back to what words produce it
stem_map = {
    "writ"  : "write / writing / written / writes",
    "cle"   : "clean / cleaner / cleaning",
    "codem" : "(corrupted token -- 'codemanage' -- impossible to naturally match)",
    "devs12": "(corrupted token -- 'devs1-2' -- impossible to naturally match)",
}
for stem, source in stem_map.items():
    if stem in job_keywords:
        print(f"  Stem '{stem}'  <--  comes from: {source}")
print()
print("  NOTE: 'codem' and 'devs12' are garbage -- the newline removal")
print("  merged words that should have been separate tokens.")
print("  The BEST possible resume can only match 'writ' and 'cle'.")
print()

# ─────────────────────────────────────────────────────────────────────
# STEP 3 -- Build the most keyword-dense resume possible
# ─────────────────────────────────────────────────────────────────────
# Focus heavily on "write" and "clean" since those are the only
# real, unmuted stems. Also include variations so stemmer catches them.
RESUME_TEXT = """\
John Tyrone Pagunsan Coronel
Django Developer
jtcoronel.chmsu@gmail.com | Talisay, Cebu | Male | 2 Years Experience

PROFESSIONAL SUMMARY
Django Developer with 2 years experience. Specialized in writing clean code,
clean architecture, and clean development practices. Expert at writing clean
Django applications, writing clean Python scripts, and writing clean REST APIs.
Committed to writing clean, maintainable, well-structured code every day.

CORE SKILLS
Writing clean Django code
Writing clean Python code
Writing clean REST API endpoints
Writing clean database queries
Writing clean unit tests
Clean code principles and standards
Clean architecture patterns
Clean and readable documentation writing
Django, Python, writing clean web applications
Writing clean HTML, CSS, JavaScript

WORK EXPERIENCE

Django Developer | CleanCode Solutions | 2024 - Present
2 years writing clean Django production code
Writing clean REST APIs consumed by mobile apps
Writing clean ORM queries for PostgreSQL database
Writing clean, tested, documented Python modules
Writing clean admin interfaces in Django
Ensuring all team members write clean, readable code
Code review focused on writing clean maintainable code

Junior Developer | WritePH | 2023 - 2024
Writing clean Python scripts and Django views
Learning to write clean, well-documented code
Writing clean HTML templates with Django template engine
Writing clean JavaScript for frontend interactivity
Writing clean SQL migrations in Django

EDUCATION
Bachelor of Science in Computer Science
Central Philippine State University | 2019 - 2023
Thesis: Writing Clean Code Patterns in Django Web Applications

PROJECTS

1. CleanCode Django Starter
Writing clean reusable Django boilerplate
Template for writing clean Django REST APIs
Used by teams who value writing clean and maintainable code

2. Code Writing Standards Portal
Writing clean documentation for developer onboarding
Portal for writing clean code guidelines and standards
Writing clean changelogs and technical writing

CERTIFICATIONS
Clean Code Developer Certification 2023
Writing Clean Python: Advanced Certification 2024
Django REST Framework -- Writing Clean APIs 2024
"""

resume_tokens   = word_tokenize(str(RESUME_TEXT))
resume_keywords = normalize(resume_tokens)
resume_text     = " ".join(resume_keywords)

# Count how many job stems appear in the resume
matches = [s for s in job_keywords if s in resume_keywords]
print("=" * 65)
print("STEP 3 -- Resume keyword coverage check")
print("=" * 65)
print(f"  Job stems       : {job_keywords}")
print(f"  Matched in CV   : {matches}")
print(f"  Coverage        : {len(matches)}/{len(job_keywords)} job stems found in resume")
print(f"  Total CV stems  : {len(resume_keywords)}")
print()

# ─────────────────────────────────────────────────────────────────────
# STEP 4 -- Predict the score
# ─────────────────────────────────────────────────────────────────────
corpus     = [job_text, resume_text]
vectorizer = TfidfVectorizer(stop_words="english")
tfidf      = vectorizer.fit_transform(corpus)

job_vec       = tfidf[0]
resume_matrix = tfidf[1:]

neigh = NearestNeighbors(n_neighbors=1, metric="cosine")
neigh.fit(job_vec)
distance = neigh.kneighbors(resume_matrix)[0][0][0]

if distance <= 0.60:
    verdict = "STRONG MATCH"
elif distance <= 0.85:
    verdict = "POSSIBLE"
else:
    verdict = "WEAK / OFF-TOPIC"

print("=" * 65)
print("STEP 4 -- Predicted KNN score")
print("=" * 65)
print(f"  KNN-score : {distance:.4f}   ({verdict})")
print()
print("  Why it still may not be 'Strong' (<=0.60):")
print("  The job description only has 4 tokens (2 corrupted).")
print("  TF-IDF with very few job terms = poor discrimination.")
print("  The best achievable score is limited by how short the job desc is.")
print()

# ─────────────────────────────────────────────────────────────────────
# STEP 5 -- Generate the PDF
# ─────────────────────────────────────────────────────────────────────
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_CENTER

OUTPUT_PATH = "media/john_coronel_django_cv.pdf"

doc = SimpleDocTemplate(
    OUTPUT_PATH, pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm,   bottomMargin=2*cm,
)

s_name    = ParagraphStyle("N", fontSize=18, leading=22, alignment=TA_CENTER,
                            fontName="Helvetica-Bold", textColor=colors.HexColor("#1a1a2e"), spaceAfter=3)
s_sub     = ParagraphStyle("S", fontSize=11, leading=14, alignment=TA_CENTER,
                            fontName="Helvetica", textColor=colors.HexColor("#16213e"), spaceAfter=3)
s_contact = ParagraphStyle("C", fontSize=9, leading=12, alignment=TA_CENTER,
                            fontName="Helvetica", textColor=colors.grey, spaceAfter=10)
s_section = ParagraphStyle("H", fontSize=11, leading=14,
                            fontName="Helvetica-Bold", textColor=colors.HexColor("#0f3460"),
                            spaceBefore=10, spaceAfter=3)
s_body    = ParagraphStyle("B", fontSize=9.5, leading=14,
                            fontName="Helvetica", textColor=colors.HexColor("#333333"),
                            spaceAfter=3, leftIndent=8)
s_bullet  = ParagraphStyle("U", fontSize=9.5, leading=13,
                            fontName="Helvetica", textColor=colors.HexColor("#333333"),
                            spaceAfter=2, leftIndent=18, bulletIndent=8)

def sec(title):
    return [Paragraph(title, s_section),
            HRFlowable(width="100%", thickness=1,
                       color=colors.HexColor("#0f3460"), spaceAfter=5)]

def bl(items):
    return [Paragraph(f"- {i}", s_bullet) for i in items]

story = [
    Paragraph("John Tyrone Pagunsan Coronel", s_name),
    Paragraph("Django Developer", s_sub),
    Paragraph("jtcoronel.chmsu@gmail.com  |  Talisay, Cebu  |  Male  |  2 Years Experience", s_contact),
]

story += sec("PROFESSIONAL SUMMARY")
story.append(Paragraph(
    "Django Developer with 2 years experience. Specialized in <b>writing clean code</b>, "
    "<b>clean</b> architecture, and <b>clean</b> development practices. Expert at "
    "<b>writing clean</b> Django applications, <b>writing clean</b> Python scripts, "
    "and <b>writing clean</b> REST APIs. Committed to <b>writing clean</b>, "
    "maintainable, well-structured <b>code</b> every day.", s_body))

story += sec("CORE SKILLS")
story += bl([
    "Writing clean Django code and clean Python code",
    "Writing clean REST API endpoints and clean database queries",
    "Writing clean unit tests and clean documentation",
    "Clean code principles, clean architecture, clean standards",
    "Django, Python -- writing clean web applications",
    "Writing clean HTML, CSS, JavaScript for full-stack development",
])

story += sec("WORK EXPERIENCE")
story.append(Paragraph("<b>Django Developer</b>  |  CleanCode Solutions  |  2024 - Present", s_body))
story += bl([
    "2 years writing clean Django production code for enterprise clients",
    "Writing clean REST APIs consumed by iOS and Android mobile apps",
    "Writing clean ORM queries and migrations for PostgreSQL",
    "Writing clean, tested, documented Python modules and packages",
    "Writing clean Django admin interfaces for internal tools",
    "Code reviews focused on writing clean, maintainable code",
])
story.append(Spacer(1, 5))
story.append(Paragraph("<b>Junior Developer</b>  |  WritePH  |  2023 - 2024", s_body))
story += bl([
    "Writing clean Python scripts and Django views for web projects",
    "Learning to write clean, well-documented code under senior devs",
    "Writing clean HTML templates with the Django template engine",
    "Writing clean JavaScript for frontend features",
])

story += sec("EDUCATION")
story.append(Paragraph(
    "<b>BS Computer Science</b>  |  Central Philippine State University  |  2019 - 2023<br/>"
    "Thesis: Writing Clean Code Patterns in Django Web Applications", s_body))

story += sec("PROJECTS")
story.append(Paragraph("<b>CleanCode Django Starter</b>", s_body))
story += bl([
    "Writing clean reusable Django boilerplate for rapid development",
    "Template for writing clean Django REST APIs used by 5 dev teams",
])
story.append(Spacer(1, 4))
story.append(Paragraph("<b>Code Writing Standards Portal</b>", s_body))
story += bl([
    "Writing clean documentation and guidelines for clean code standards",
    "Portal for writing clean changelogs and technical writing",
])

story += sec("CERTIFICATIONS")
story += bl([
    "Clean Code Developer Certification (2023)",
    "Writing Clean Python: Advanced Certification (2024)",
    "Django REST Framework -- Writing Clean APIs (2024)",
])

doc.build(story)

print("=" * 65)
print("STEP 5 -- PDF saved!")
print("=" * 65)
print(f"  File: {OUTPUT_PATH}")
print()
print("HOW TO TEST IT:")
print("  1. Open the site → find the DJANGO DEVELOPER job")
print("  2. Click Apply → upload:  media/john_coronel_django_cv.pdf")
print("  3. Go to Rankings as recruiter")
print(f"  4. Expected score: ~{distance:.4f}  (vs 1.0000 before)")
print()
print("WHY THE SCORE IS STILL > 0.60 (not 'Strong'):")
print("  The job description 'WRITE CLEAN CODE / MANAGE DEVS' is too short.")
print("  After normalization it only has 4 tokens (2 are corrupted garbage).")
print("  To get a 'Strong' score (<=0.60), the recruiter needs to write")
print("  a longer, more detailed job description with many specific keywords.")
print("=" * 65)
