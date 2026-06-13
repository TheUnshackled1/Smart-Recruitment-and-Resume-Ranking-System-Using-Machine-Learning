# -*- coding: utf-8 -*-
"""Generate 3 optimized resume PDFs for all 3 job listings, named John Doe."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))

import nltk
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

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
            HRFlowable(width="100%", thickness=1,
                       color=colors.HexColor("#0f3460"), spaceAfter=5)]

def bl(items, s_bullet):
    return [Paragraph("- " + i, s_bullet) for i in items]

def save(path, story):
    doc = SimpleDocTemplate(path, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    doc.build(story)
    size = pathlib.Path(path).stat().st_size
    print(f"Saved: {path}  ({size:,} bytes)")


# ════════════════════════════════════════════════════════════════════
# PDF 1 — Circle FinTech: Senior Software Engineer, Python/Django
# ════════════════════════════════════════════════════════════════════
st = make_styles()
s_name, s_sub, s_contact, s_section, s_body, s_bullet = st

story1 = [
    Paragraph("John Doe", s_name),
    Paragraph("Senior Software Engineer | Python / Django Developer", s_sub),
    Paragraph("johndoe@email.com  |  Talisay, LSAB 310  |  Male  |  2 Years Experience", s_contact),
]
story1 += sec("PROFESSIONAL SUMMARY", s_section)
story1.append(Paragraph(
    "Senior Python and Django Developer experienced in developing backend systems for banking "
    "and financial institutions. Committed to solving problems collaboratively, following design "
    "patterns, and delivering scalable, robust, quality software. Skilled in architecture patterns, "
    "API integration, database design, unit tests, code reviews, automation, and writing "
    "documentation for all code produced. Quickly adapts to new technologies and platforms "
    "to write production-ready code and deliver results on schedule.", s_body))

story1 += sec("CORE SKILLS", s_section)
story1 += bl([
    "Python and Django -- developing backend systems for banking mobile applications",
    "Build robust and scalable software following design patterns and architecture patterns",
    "Integration of user-facing elements with server-side logic",
    "Building reusable code and libraries for future use",
    "Optimization of application for maximum speed and scalability",
    "Implementation of security and data protection",
    "Design and implementation of data storage solutions",
    "Different types of API integration and Cross-team Collaboration",
    "Write documentation of all codes produced and update/upgrade whenever applicable",
    "Writing unit tests, automation, and performing code reviews to improve code quality",
    "Participate in database and API design and provide inputs or run tests when necessary",
    "Learn and adapt to new technologies/platforms and write production codes with it",
    "Contribute ideas to technology, algorithms, and products in brainstorming sessions",
    "Dive into difficult problems and successfully deliver results on schedule",
], s_bullet)

story1 += sec("WORK EXPERIENCE", s_section)
story1.append(Paragraph("<b>Senior Python/Django Developer</b>  |  BankTech Solutions  |  2024 - Present", s_body))
story1 += bl([
    "Responsible for development, maintenance and deployment of banking mobile applications",
    "Developing backend systems for different banks and financial institutions",
    "Build robust and scalable software following proper architecture patterns and smart code",
    "Integration of user-facing elements developed with server-side logic",
    "Building reusable code and libraries for future use across multiple projects",
    "Optimization of application for maximum speed and scalability",
    "Implementation of security and data protection for sensitive financial data",
    "Design and implementation of data storage solutions for banking systems",
    "Different types of API integration for payment gateways and financial institutions",
    "Cross-team Collaboration for developing the best solutions",
    "Write documentation of all codes produced and update/upgrade them whenever applicable",
    "Participate in database and API design and provide inputs or run tests when necessary",
    "Learn and adapt to new technologies/platforms when needed and write production codes",
    "Help improve code quality through writing unit tests, automation and code reviews",
    "Participate in brainstorming sessions and contribute ideas to technology and products",
    "Dive into difficult problems and successfully deliver results on schedule",
], s_bullet)
story1.append(Spacer(1, 5))
story1.append(Paragraph("<b>Junior Django Developer</b>  |  FinTech PH  |  2023 - 2024", s_body))
story1 += bl([
    "Developing backend systems for mobile applications using Python and Django",
    "Building reusable code and libraries for future use in financial services",
    "Learned to adapt to new technologies/platforms and write production codes with it",
    "Participated in database and API design and provided inputs and run tests when necessary",
    "Contributed ideas to technology, algorithms, and products in brainstorming sessions",
], s_bullet)

story1 += sec("EDUCATION", s_section)
story1.append(Paragraph(
    "<b>BS Computer Science</b>  |  Central Philippine State University  |  2019 - 2023<br/>"
    "Thesis: Scalable Django Backend Architecture for Banking Mobile Applications", s_body))

story1 += sec("PROJECTS", s_section)
story1.append(Paragraph("<b>Banking API Integration Platform (Python/Django)</b>", s_body))
story1 += bl([
    "Developing backend systems for different banks following proper architecture patterns",
    "Build robust and scalable software -- building reusable code and libraries for future use",
    "Implementation of security and data protection and data storage solutions",
    "Different types of API integration -- Cross-team Collaboration for best solutions",
    "Wrote documentation of all codes produced and updated/upgraded whenever applicable",
    "Helped improve code quality through writing unit tests, automation and code reviews",
], s_bullet)

story1 += sec("CERTIFICATIONS", s_section)
story1 += bl([
    "Python Django Developer Certification (2023)",
    "Banking Software Architecture and API Integration (2024)",
    "Unit Testing, Automation and Code Review Best Practices (2024)",
], s_bullet)

save("media/john_doe_senior_django_cv.pdf", story1)


# ════════════════════════════════════════════════════════════════════
# PDF 2 — Reve Systems: Web Developer
# ════════════════════════════════════════════════════════════════════
st = make_styles()
s_name, s_sub, s_contact, s_section, s_body, s_bullet = st

story2 = [
    Paragraph("John Doe", s_name),
    Paragraph("Web Developer | Full Stack Developer", s_sub),
    Paragraph("johndoe@email.com  |  Bacolod, CHMSU  |  Male  |  1 Year Experience", s_contact),
]
story2 += sec("PROFESSIONAL SUMMARY", s_section)
story2.append(Paragraph(
    "Fresh web developer with good working knowledge on web developing. Very good knowledge "
    "of Java, JSP, HTML/CSS/JavaScript and MySQL database. Familiar with MVC pattern and "
    "advanced knowledge of HTML, CSS, and JavaScript. Excellent capability to handle database "
    "especially MySQL and MongoDB. Excellent capability to translate complex client requirements "
    "to technical implementation. Hardworking, innovative, good communication skills, and "
    "persists under pressure. Fair understanding of building RESTful APIs.", s_body))

story2 += sec("CORE SKILLS", s_section)
story2 += bl([
    "Web developing -- good working knowledge of HTML/CSS/JavaScript",
    "Very good knowledge of Java and JSP for server-side web developing",
    "Excellent capability to handle database especially MySQL and MongoDB",
    "Familiar with MVC pattern and advanced knowledge of HTML/CSS/JavaScript",
    "Integration of user-facing elements developed by front-end developer with server-side logic",
    "Building reusable code and libraries for future use",
    "Optimization of application for maximum speed and scalability",
    "Implementation of security and data protection",
    "Design and implementation of data architecture storage solutions",
    "Supervise server resources and cross-platform optimization across Internet browsers",
    "Use databases, web servers, wireframe development, and UI/UX design in development",
    "Working knowledge of MongoDB and MySQL",
    "Fair understanding of building RESTful APIs",
    "Great communication skill -- translate complex client requirements to technical implementation",
    "Hardworking, innovative, good communication skills, and persist under pressure",
], s_bullet)

story2 += sec("WORK EXPERIENCE", s_section)
story2.append(Paragraph("<b>Junior Web Developer</b>  |  WebPH Solutions  |  2024 - Present", s_body))
story2 += bl([
    "Web developing using HTML/CSS/JavaScript, Java, and JSP for client web applications",
    "Very good knowledge of Java and JSP applied in server-side web developing",
    "Integration of user-facing elements developed by front-end developer with server-side logic",
    "Building reusable code and libraries for future use and optimization for speed and scalability",
    "Excellent capability to handle database especially MySQL -- database design and queries",
    "Working knowledge of MongoDB and MySQL applied daily for web developing projects",
    "Implementation of security and data protection for web applications",
    "Design and implementation of data architecture storage solutions",
    "Supervised server resources and cross-platform optimization across Internet browsers",
    "Used databases, web servers, wireframe development, and UI/UX design in the development procedure",
    "Fair understanding of building RESTful APIs -- built and integrated web services",
    "Great communication skill -- excellent capability to translate complex client requirements",
    "Hardworking and innovative -- persist under pressure during tight deadlines",
], s_bullet)
story2.append(Spacer(1, 5))
story2.append(Paragraph("<b>Web Development Intern</b>  |  StartupBacolod  |  2023 - 2024", s_body))
story2 += bl([
    "Good working knowledge of HTML/CSS/JavaScript for web developing",
    "Familiar with MVC pattern applied in Java/JSP web developing projects",
    "Excellent capability to handle database especially MySQL for data management",
    "Fair understanding of building RESTful APIs and web server management",
    "Good communication skills in translating complex client requirements to technical implementation",
    "Hardworking, innovative, and persists under pressure in fast-paced startup environment",
], s_bullet)

story2 += sec("EDUCATION", s_section)
story2.append(Paragraph(
    "<b>BS Computer Science</b>  |  CHMSU, Bacolod  |  2019 - 2023<br/>"
    "Thesis: Web Developing with Java/JSP and MySQL using MVC Pattern", s_body))

story2 += sec("PROJECTS", s_section)
story2.append(Paragraph("<b>Full Stack Web App (Java/JSP + MySQL)</b>", s_body))
story2 += bl([
    "Very good knowledge of Java and JSP -- built complete server-side web developing project",
    "Excellent capability to handle database especially MySQL -- managed 10,000+ records",
    "Familiar with MVC pattern -- used throughout the web developing architecture",
    "Implementation of security and data protection for user data",
    "Cross-platform optimization across Internet browsers and operating systems",
], s_bullet)
story2.append(Spacer(1, 4))
story2.append(Paragraph("<b>RESTful API Service (HTML/CSS/JavaScript + MongoDB)</b>", s_body))
story2 += bl([
    "Fair understanding of building RESTful APIs -- designed and deployed RESTful web service",
    "Working knowledge of MongoDB as primary database for the RESTful API project",
    "Advanced knowledge of HTML/CSS/JavaScript for the front-end of the web service",
    "Used web servers, wireframe development, and UI/UX design in the development procedure",
    "Great communication skill -- translated complex client requirements to technical implementation",
], s_bullet)

story2 += sec("CERTIFICATIONS", s_section)
story2 += bl([
    "Web Developer Certification -- HTML/CSS/JavaScript (2023)",
    "Java and JSP Server-Side Web Developing (2024)",
    "MySQL and MongoDB Database Management (2024)",
    "RESTful API Design and MVC Pattern Certification (2024)",
], s_bullet)

save("media/john_doe_webdev_cv.pdf", story2)


# ════════════════════════════════════════════════════════════════════
# PDF 3 — DROPBOX: Django Developer
# ════════════════════════════════════════════════════════════════════
st = make_styles()
s_name, s_sub, s_contact, s_section, s_body, s_bullet = st

story3 = [
    Paragraph("John Doe", s_name),
    Paragraph("Django Developer | Python Web Developer", s_sub),
    Paragraph("johndoe@email.com  |  Talisay  |  Male  |  1.5 Years Experience", s_contact),
]
story3 += sec("PROFESSIONAL SUMMARY", s_section)
story3.append(Paragraph(
    "Django Developer experienced in writing clean code and managing dev teams. "
    "Committed to writing clean, maintainable, and well-structured code every day. "
    "Skilled at managing developers and ensuring the dev team follows clean code "
    "standards. Expert in writing clean Django applications, writing clean Python scripts, "
    "and writing clean REST APIs while managing devs through the full development lifecycle.", s_body))

story3 += sec("CORE SKILLS", s_section)
story3 += bl([
    "Writing clean Django code and clean Python code",
    "Writing clean REST API endpoints and clean database queries",
    "Writing clean unit tests and clean technical documentation",
    "Clean code principles, clean architecture, and clean coding standards",
    "Managing dev team and managing developers through project lifecycle",
    "Writing clean HTML, CSS, JavaScript for full-stack Django development",
    "Writing clean ORM queries, migrations, and Django admin interfaces",
    "Managing devs during sprint planning, standups, and code reviews",
    "Writing clean, testable, well-documented Django modules and packages",
], s_bullet)

story3 += sec("WORK EXPERIENCE", s_section)
story3.append(Paragraph("<b>Django Developer</b>  |  CleanCode Solutions  |  2024 - Present", s_body))
story3 += bl([
    "Writing clean Django code for multiple production web applications",
    "Managing dev team of 3 junior developers across all active projects",
    "Writing clean REST APIs using Django REST Framework for mobile clients",
    "Writing clean ORM queries and database migrations for PostgreSQL",
    "Writing clean unit tests and automation scripts for Django applications",
    "Managing developers during sprint planning, daily standups, and retrospectives",
    "Code reviews enforcing clean code standards -- managing devs to write clean code",
    "Writing clean documentation for all Django modules produced",
    "Writing clean, reusable Django components shared across the dev team",
], s_bullet)
story3.append(Spacer(1, 5))
story3.append(Paragraph("<b>Junior Django Developer</b>  |  WritePH  |  2023 - 2024", s_body))
story3 += bl([
    "Writing clean Python and Django code for customer-facing web applications",
    "Assisted in managing dev task allocation and developer schedules",
    "Writing clean HTML templates using Django template engine",
    "Writing clean JavaScript for frontend interactive features",
    "Learned clean code best practices under a senior Django developer",
], s_bullet)

story3 += sec("EDUCATION", s_section)
story3.append(Paragraph(
    "<b>BS Computer Science</b>  |  Central Philippine State University  |  2019 - 2023<br/>"
    "Thesis: Writing Clean Code Patterns in Django Web Applications", s_body))

story3 += sec("PROJECTS", s_section)
story3.append(Paragraph("<b>CleanCode Django Starter Kit</b>", s_body))
story3 += bl([
    "Writing clean reusable Django boilerplate for rapid development",
    "Template for writing clean Django REST APIs used by 5 dev teams",
    "Managing devs who contribute -- code reviews to ensure clean code",
], s_bullet)
story3.append(Spacer(1, 4))
story3.append(Paragraph("<b>Dev Team Management Portal (Django)</b>", s_body))
story3 += bl([
    "Writing clean Django app for managing developers and dev team workflows",
    "Managing devs -- track clean code metrics, sprint progress, and code reviews",
    "Writing clean documentation and clean API endpoints for the management portal",
], s_bullet)

story3 += sec("CERTIFICATIONS", s_section)
story3 += bl([
    "Clean Code Developer Certification (2023)",
    "Writing Clean Python and Django -- Advanced Certification (2024)",
    "Managing Dev Teams -- Agile Certification (2024)",
], s_bullet)

save("media/john_doe_django_cv.pdf", story3)

print("\nAll 3 resumes for John Doe generated successfully!")
print("  1. media/john_doe_senior_django_cv.pdf  -- Circle FinTech (Senior Software Engineer)")
print("  2. media/john_doe_webdev_cv.pdf         -- Reve Systems (Web Developer)")
print("  3. media/john_doe_django_cv.pdf         -- DROPBOX (Django Developer)")
