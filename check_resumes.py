# -*- coding: utf-8 -*-
"""
Diagnostic script: checks each PDF in the resumes/ folder
- Can text be extracted?
- How many words after normalization?
- Sample KNN score against a dummy job description
Run from the project root:  python check_resumes.py
"""
import pathlib, re, sys
import PyPDF2

RESUME_DIR = pathlib.Path("resumes")

def extract_text(pdf_path):
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f, strict=False)
            text = ""
            for page in reader.pages:
                text += (page.extract_text() or "")
        text = re.sub(r"\s+", " ", text).strip()
        return text
    except Exception as e:
        return f"ERROR: {e}"

print(f"\n{'='*70}")
print(f"{'FILE':<45} {'CHARS':>7}  {'STATUS'}")
print(f"{'='*70}")

results = []
for pdf in sorted(RESUME_DIR.glob("*.pdf")):
    text = extract_text(pdf)
    if text.startswith("ERROR"):
        status = text
        chars = 0
    elif len(text) == 0:
        status = "[!] EMPTY  -- likely a scanned/image PDF, cannot be ranked"
        chars = 0
    elif len(text) < 200:
        status = "[!] VERY SHORT -- minimal extractable text"
        chars = len(text)
    else:
        status = "[OK]"
        chars = len(text)
    results.append((pdf.name, chars, status, text))
    print(f"{pdf.name:<45} {chars:>7}  {status}")

# -------------------------------------------------------------------
# Quick TF-IDF / cosine demo using a generic software-engineer job desc
# -------------------------------------------------------------------
print(f"\n{'='*70}")
print("QUICK SCORE DEMO vs. a generic Software Engineer job description")
print(f"{'='*70}")

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.neighbors import NearestNeighbors
    import nltk
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)
    from nltk.tokenize import word_tokenize

    # Add project to path so we can import normalize()
    sys.path.insert(0, str(pathlib.Path(__file__).parent))
    from mysite.text_process import normalize

    sample_job = (
        "Software Engineer Python Django REST API machine learning NLP "
        "data structures algorithms SQL PostgreSQL Git CI/CD Agile team "
        "communication problem solving bachelor degree computer science"
    )
    try:
        job_text = " ".join(normalize(word_tokenize(sample_job)))
    except Exception:
        job_text = sample_job

    good = [(name, text) for name, chars, status, text in results if chars > 200]
    if not good:
        print("No usable resume text found.")
    else:
        resume_texts = []
        resume_names = []
        for name, text in good:
            try:
                norm = " ".join(normalize(word_tokenize(text)))
            except Exception:
                norm = text
            resume_texts.append(norm)
            resume_names.append(name)

        corpus = [job_text] + resume_texts
        vec = TfidfVectorizer(stop_words="english")
        tfidf = vec.fit_transform(corpus)
        job_vec = tfidf[0]
        resume_matrix = tfidf[1:]
        neigh = NearestNeighbors(n_neighbors=1, metric="cosine")
        neigh.fit(job_vec)
        distances = neigh.kneighbors(resume_matrix)[0][:, 0]

        scored = sorted(zip(resume_names, distances), key=lambda x: x[1])
        print(f"\n{'RANK':<5} {'SCORE':>7}  {'VERDICT':<18} {'FILE'}")
        print("-" * 70)
        for rank, (name, dist) in enumerate(scored, 1):
            if dist <= 0.60:
                verdict = "[STRONG]"
            elif dist <= 0.85:
                verdict = "[POSSIBLE]"
            else:
                verdict = "[WEAK/OFF-TOPIC]"
            print(f"{rank:<5} {dist:>7.4f}  {verdict:<18} {name}")

except ImportError as e:
    print(f"sklearn/nltk not available in this environment: {e}")

print(f"\n{'='*70}")
print("WHY score = 1.0000 (worst possible)?")
print("  Cosine distance of 1.0 means ZERO shared vocabulary between")
print("  your CV and the job description after normalization.")
print("  Common causes:")
print("  1. The uploaded CV is a scanned image — PyPDF2 extracts NO text.")
print("  2. The CV is in a different language/domain from the job posting.")
print("  3. The job description itself has very few keywords.")
print("  4. The CV was uploaded in a format that wasn't parsed (e.g. .doc).")
print(f"{'='*70}\n")
