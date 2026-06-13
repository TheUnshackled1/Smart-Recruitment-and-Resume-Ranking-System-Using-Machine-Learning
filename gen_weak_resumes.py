# -*- coding: utf-8 -*-
"""Generate OFF-TOPIC resume PDFs to test the > 0.85 (Weak) scoring."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_CENTER

def make_styles():
    s_name    = ParagraphStyle("N",  fontSize=18, leading=22, alignment=TA_CENTER,
                               fontName="Helvetica-Bold", textColor=colors.HexColor("#1a1a2e"), spaceAfter=3)
    s_sub     = ParagraphStyle("S",  fontSize=11, leading=14, alignment=TA_CENTER,
                               fontName="Helvetica", textColor=colors.HexColor("#16213e"), spaceAfter=3)
    s_contact = ParagraphStyle("C",  fontSize=9,  leading=12, alignment=TA_CENTER,
                               fontName="Helvetica", textColor=colors.grey, spaceAfter=10)
    s_section = ParagraphStyle("H",  fontSize=11, leading=14,
                               fontName="Helvetica-Bold", textColor=colors.HexColor("#0f3460"),
                               spaceBefore=10, spaceAfter=3)
    s_body    = ParagraphStyle("B",  fontSize=9.5, leading=14,
                               fontName="Helvetica", textColor=colors.HexColor("#333333"),
                               spaceAfter=3, leftIndent=8)
    s_bullet  = ParagraphStyle("U",  fontSize=9.5, leading=13,
                               fontName="Helvetica", textColor=colors.HexColor("#333333"),
                               spaceAfter=2, leftIndent=18)
    return s_name, s_sub, s_contact, s_section, s_body, s_bullet

def sec(title, s_section):
    return [Paragraph(title, s_section),
            HRFlowable(width="100%", thickness=1, color=colors.HexColor("#0f3460"), spaceAfter=5)]

def bl(items, s_bullet):
    return [Paragraph("- " + i, s_bullet) for i in items]

def save(path, story):
    doc = SimpleDocTemplate(path, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    doc.build(story)
    size = pathlib.Path(path).stat().st_size
    print(f"Saved: {path}  ({size:,} bytes)")


st = make_styles()
s_name, s_sub, s_contact, s_section, s_body, s_bullet = st

# =====================================================================
# 1. Circle FinTech - Weak CV (Fitness Trainer)
# Completely unrelated to Python, Django, Backend, Banks, APIs, etc.
# =====================================================================
def generate_fitness_cv(name, filename):
    story = [
        Paragraph(name, s_name),
        Paragraph("Certified Personal Fitness Trainer", s_sub),
        Paragraph("contact@email.com  |  Talisay  |  Male  |  5 Years Experience", s_contact),
    ]
    story += sec("PROFESSIONAL SUMMARY", s_section)
    story.append(Paragraph(
        "Highly motivated Personal Trainer with 5 years of experience helping clients achieve "
        "their fitness and weight loss goals. Expert in creating customized workout plans, "
        "dietary guidelines, and aerobic exercise routines. Passionate about health, nutrition, "
        "and physical well-being. Not familiar with any programming languages or software engineering.", s_body))
    
    story += sec("CORE SKILLS", s_section)
    story += bl([
        "Personal Training and Workout Planning",
        "Nutritional Counseling and Diet Planning",
        "Cardiovascular Endurance Training",
        "Weightlifting and Strength Conditioning",
        "First Aid and CPR Certified",
        "Motivation and Goal Setting for Clients"
    ], s_bullet)

    story += sec("WORK EXPERIENCE", s_section)
    story.append(Paragraph("<b>Head Personal Trainer</b>  |  Talisay Gym & Fitness  |  2021 - Present", s_body))
    story += bl([
        "Managed a team of 4 junior fitness instructors",
        "Created custom workout regimens for over 50 active clients",
        "Conducted weekly group aerobic and yoga sessions",
        "Maintained gym equipment and ensured safety standards were met"
    ], s_bullet)

    story += sec("EDUCATION", s_section)
    story.append(Paragraph("<b>BS Physical Education</b>  |  Sports University  |  2015 - 2019", s_body))
    
    save(filename, story)

# =====================================================================
# 2. Reve Systems - Weak CV (Culinary Chef)
# Completely unrelated to Web Dev, Java, JSP, MySQL, HTML/CSS/JS, MVC
# =====================================================================
def generate_chef_cv(name, filename):
    story = [
        Paragraph(name, s_name),
        Paragraph("Executive Chef | Culinary Arts", s_sub),
        Paragraph("contact@email.com  |  Bacolod  |  Male  |  8 Years Experience", s_contact),
    ]
    story += sec("PROFESSIONAL SUMMARY", s_section)
    story.append(Paragraph(
        "Creative and passionate Executive Chef with 8 years of experience in fine dining "
        "and banquet catering. Expert in French and Italian cuisines, menu development, "
        "and kitchen management. Dedicated to delivering exceptional culinary experiences "
        "using locally sourced ingredients. Zero experience with web development or databases.", s_body))
    
    story += sec("CORE SKILLS", s_section)
    story += bl([
        "Menu Development and Recipe Creation",
        "Food Safety and Sanitation (ServSafe Certified)",
        "Inventory Management and Food Cost Control",
        "Baking and Pastry Arts",
        "Kitchen Staff Hiring and Training",
        "High-Volume Catering and Event Planning"
    ], s_bullet)

    story += sec("WORK EXPERIENCE", s_section)
    story.append(Paragraph("<b>Executive Chef</b>  |  Le Grand Restaurant  |  2019 - Present", s_body))
    story += bl([
        "Designed and implemented seasonal menus that increased revenue by 20%",
        "Managed a kitchen staff of 15 cooks, sous chefs, and dishwashers",
        "Maintained strict hygiene standards and passed all health inspections with 100%",
        "Negotiated with local farmers for fresh produce deliveries"
    ], s_bullet)

    story += sec("EDUCATION", s_section)
    story.append(Paragraph("<b>Diploma in Culinary Arts</b>  |  Bacolod Culinary Institute  |  2013 - 2015", s_body))
    
    save(filename, story)

# =====================================================================
# 3. DROPBOX - Weak CV (Marine Biologist)
# Completely unrelated to Django, Python, Clean Code, Managing Devs
# =====================================================================
def generate_marine_cv(name, filename):
    story = [
        Paragraph(name, s_name),
        Paragraph("Marine Biologist | Ocean Researcher", s_sub),
        Paragraph("contact@email.com  |  Coastal City  |  Male  |  3 Years Experience", s_contact),
    ]
    story += sec("PROFESSIONAL SUMMARY", s_section)
    story.append(Paragraph(
        "Dedicated Marine Biologist focusing on coral reef conservation and marine ecology. "
        "Experienced in underwater field research, scuba diving, and marine species identification. "
        "Passionate about ocean conservation and studying the effects of climate change on "
        "marine ecosystems. I do not write code or manage software developers.", s_body))
    
    story += sec("CORE SKILLS", s_section)
    story += bl([
        "Marine Species Identification",
        "Coral Reef Health Assessment",
        "Scuba Diving (PADI Advanced Certified)",
        "Water Quality Testing and Sampling",
        "Wildlife Conservation and Rehabilitation",
        "Field Research and Data Collection"
    ], s_bullet)

    story += sec("WORK EXPERIENCE", s_section)
    story.append(Paragraph("<b>Marine Research Assistant</b>  |  Oceanic Institute  |  2022 - Present", s_body))
    story += bl([
        "Conducted underwater surveys of coral bleaching events",
        "Collected water samples to measure salinity and pH levels",
        "Assisted in the rescue and rehabilitation of sea turtles",
        "Published findings in the Journal of Marine Conservation"
    ], s_bullet)

    story += sec("EDUCATION", s_section)
    story.append(Paragraph("<b>BS Marine Biology</b>  |  Coastal University  |  2018 - 2022", s_body))
    
    save(filename, story)


# Generate the 6 PDFs
print("Generating Weak / Off-topic CVs for John Tyrone Coronel...")
generate_fitness_cv("John Tyrone Coronel", "media/john_tyrone_weak_circle_fintech.pdf")
generate_chef_cv("John Tyrone Coronel", "media/john_tyrone_weak_reve_systems.pdf")
generate_marine_cv("John Tyrone Coronel", "media/john_tyrone_weak_dropbox.pdf")

print("\nGenerating Weak / Off-topic CVs for John Doe...")
generate_fitness_cv("John Doe", "media/john_doe_weak_circle_fintech.pdf")
generate_chef_cv("John Doe", "media/john_doe_weak_reve_systems.pdf")
generate_marine_cv("John Doe", "media/john_doe_weak_dropbox.pdf")

print("\nDone! All 6 off-topic resumes have been generated.")
