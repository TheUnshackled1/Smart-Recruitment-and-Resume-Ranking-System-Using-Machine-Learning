# -*- coding: utf-8 -*-
"""Generate 2 optimized resume PDFs for Circle FinTech and Reve Systems jobs."""
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
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# ── shared styles ────────────────────────────────────────────────────
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

def sec(title, s_section, s_hr_color="#0f3460"):
    return [Paragraph(title, s_section),
            HRFlowable(width="100%", thickness=1, color=colors.HexColor(s_hr_color), spaceAfter=5)]

def bl(items, s_bullet):
    return [Paragraph("- " + i, s_bullet) for i in items]

def build_pdf(output_path, story):
    doc = SimpleDocTemplate(output_path, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    doc.build(story)
    print("Saved: " + output_path)


# ════════════════════════════════════════════════════════════════════
# PDF 1 — Circle FinTech: Senior Software Engineer, Python/Django
# ════════════════════════════════════════════════════════════════════
s_name, s_sub, s_contact, s_section, s_body, s_bullet = make_styles()
story1 = [
    Paragraph("John Tyrone Pagunsan Coronel", s_name),
    Paragraph("Senior Software Engineer | Python / Django Developer", s_sub),
    Paragraph("jtcoronel.chmsu@gmail.com  |  Talisay, LSAB 310  |  Male  |  2 Years Experience", s_contact),
]

story1 += sec("PROFESSIONAL SUMMARY", s_section)
story1.append(Paragraph(
    "Senior Python and Django Developer with experience in developing backend systems for "
    "banking and financial institutions. Committed to solving problems collaboratively, "
    "following design patterns, and delivering scalable, robust, quality software. "
    "Experienced in architecture patterns, API integration, database design, unit tests, "
    "code reviews, automation, and writing documentation for all code produced. "
    "Adapts quickly to new technologies and platforms to write production-ready code.", s_body))

story1 += sec("CORE SKILLS", s_section)
story1 += bl([
    "Python / Django development -- backend systems and REST API integration",
    "Build robust and scalable software following design patterns and architecture patterns",
    "Integration of user-facing elements with server-side logic",
    "Building reusable code and libraries for future use",
    "Optimization of application performance, speed, and scalability",
    "Implementation of security and data protection solutions",
    "Design and implementation of data storage solutions",
    "Different types of API integration and Cross-team Collaboration",
    "Writing documentation for all codes produced and update/upgrade when applicable",
    "Writing unit tests, automation, and performing code reviews",
    "Database and API design -- participate and provide inputs or run tests when necessary",
    "Dive into difficult problems and deliver results on schedule",
    "Brainstorming sessions -- contribute ideas to technology, algorithms, and products",
    "Learn and adapt to new technologies and write production codes with it",
], s_bullet)

story1 += sec("WORK EXPERIENCE", s_section)
story1.append(Paragraph("<b>Senior Python/Django Developer</b>  |  BankTech Solutions  |  2024 - Present", s_body))
story1 += bl([
    "Developing backend systems for banking mobile applications using Python and Django",
    "Build robust and scalable software following proper architecture patterns and smart code",
    "Integration of user-facing elements developed with server-side logic for 3 bank clients",
    "Building reusable code and libraries for future use across multiple financial institution projects",
    "Optimization of application for maximum speed and scalability under high banking load",
    "Implementation of security and data protection for sensitive financial data",
    "Design and implementation of data storage solutions for banking transaction systems",
    "Different types of API integration for payment gateways and financial institutions",
    "Cross-team Collaboration for developing the best solutions across 4 development teams",
    "Write documentation for all codes produced and update/upgrade them whenever applicable",
    "Participate in database and API design and provide inputs or run tests when necessary",
    "Help improve code quality through writing unit tests, automation and code reviews",
    "Contribute ideas to technology, algorithms, and products during brainstorming sessions",
    "Successfully deliver results on schedule even for difficult problems",
], s_bullet)
story1.append(Spacer(1, 5))
story1.append(Paragraph("<b>Junior Django Developer</b>  |  FinTech PH  |  2023 - 2024", s_body))
story1 += bl([
    "Developing backend systems for mobile applications using Python and Django framework",
    "Building reusable code and libraries for future use in financial services platform",
    "Learned to adapt to new technologies and platforms and write production codes with it",
    "Participated in database and API design and provided inputs when necessary",
    "Participated in brainstorming sessions and contributed ideas to products and algorithms",
], s_bullet)

story1 += sec("EDUCATION", s_section)
story1.append(Paragraph(
    "<b>BS Computer Science</b>  |  Central Philippine State University  |  2019 - 2023<br/>"
    "Thesis: Scalable Django Backend Architecture for Banking Mobile Applications", s_body))

story1 += sec("PROJECTS", s_section)
story1.append(Paragraph("<b>Banking API Integration Platform (Django)</b>", s_body))
story1 += bl([
    "Developed backend systems for different banks following proper architecture patterns",
    "Built robust and scalable software with reusable code and libraries for future use",
    "Implemented security and data protection and data storage solutions for financial data",
    "Different types of API integration for financial institutions -- collaborated cross-team",
], s_bullet)
story1.append(Spacer(1, 4))
story1.append(Paragraph("<b>Mobile Banking Backend System</b>", s_body))
story1 += bl([
    "Responsible for development, maintenance and deployment of banking mobile application",
    "Optimization of application for maximum speed and scalability under concurrent load",
    "Wrote documentation for all codes produced and updated them whenever applicable",
    "Wrote unit tests, automation scripts, and performed code reviews for quality products",
], s_bullet)

story1 += sec("CERTIFICATIONS", s_section)
story1 += bl([
    "Python Django Developer Certification (2023)",
    "Banking Software Architecture Certification (2024)",
    "Scalable API Design and Data Protection Certification (2024)",
    "Unit Testing and Code Review Best Practices (2024)",
], s_bullet)

build_pdf("media/john_coronel_senior_django_cv.pdf", story1)


# ════════════════════════════════════════════════════════════════════
# PDF 2 — Reve Systems: Web Developer
# ════════════════════════════════════════════════════════════════════
s_name, s_sub, s_contact, s_section, s_body, s_bullet = make_styles()
story2 = [
    Paragraph("John Tyrone Pagunsan Coronel", s_name),
    Paragraph("Web Developer | Full Stack Developer", s_sub),
    Paragraph("jtcoronel.chmsu@gmail.com  |  Bacolod, CHMSU  |  Male  |  1 Year Experience", s_contact),
]

story2 += sec("PROFESSIONAL SUMMARY", s_section)
story2.append(Paragraph(
    "Fresh web developer with good working knowledge on web developing. "
    "Very good knowledge of Java, JSP, HTML/CSS/JavaScript and MySQL database. "
    "Familiar with MVC pattern and advanced knowledge of HTML, CSS, and JavaScript. "
    "Excellent capability to handle database especially MySQL and MongoDB. "
    "Excellent capability to translate complex client requirements to technical implementation. "
    "Hardworking, innovative, good communication skills, and persists under pressure. "
    "Good working knowledge of RESTful APIs, web servers, and UI/UX design.", s_body))

story2 += sec("CORE SKILLS", s_section)
story2 += bl([
    "Web developing -- good working knowledge of HTML/CSS/JavaScript and web development",
    "Very good knowledge of Java and JSP for server-side web developing",
    "Excellent capability to handle database especially MySQL and MongoDB",
    "Familiar with MVC pattern and advanced knowledge of HTML/CSS/JavaScript",
    "Integration of user-facing elements developed by front-end developer with server-side logic",
    "Building reusable code and libraries for future use and optimization for speed and scalability",
    "Implementation of security and data protection and data architecture storage solutions",
    "Supervise server resources and cross-platform optimization across Internet browsers",
    "Use databases, web servers, wireframe development, and UI/UX design in development",
    "Working knowledge of MongoDB and MySQL database management",
    "Fair understanding of building RESTful APIs",
    "Great communication skill -- translate complex client requirements to technical implementation",
    "Hardworking, innovative, persists under pressure with good communication skills",
], s_bullet)

story2 += sec("WORK EXPERIENCE", s_section)
story2.append(Paragraph("<b>Junior Web Developer</b>  |  WebPH Solutions  |  2024 - Present", s_body))
story2 += bl([
    "Web developing using HTML/CSS/JavaScript, Java, JSP for client web applications",
    "Very good knowledge of Java and JSP applied in server-side web developing projects",
    "Integration of user-facing elements developed by front-end developer with server-side logic",
    "Building reusable code and libraries for future use and optimization of application speed",
    "Handled database especially MySQL -- excellent capability in database design and queries",
    "Worked with MongoDB for NoSQL database storage -- working knowledge applied daily",
    "Implementation of security and data protection in web developing projects",
    "Design and implementation of data architecture storage solutions for web applications",
    "Supervised server resources and cross-platform optimization across Internet browsers",
    "Used web servers, wireframe development, and UI/UX design in the development procedure",
    "Built RESTful APIs -- fair understanding of RESTful API design and implementation",
    "Great communication skill in translating complex client requirements to technical implementation",
    "Hardworking and innovative -- persists under pressure during tight deadlines",
], s_bullet)
story2.append(Spacer(1, 5))
story2.append(Paragraph("<b>Web Development Intern</b>  |  StartupBacolod  |  2023 - 2024", s_body))
story2 += bl([
    "Good working knowledge of HTML/CSS/JavaScript for web developing projects",
    "Familiar with MVC pattern applied in Java/JSP and Django web developing",
    "Excellent capability to handle database especially MySQL for data management",
    "Learned fair understanding of building RESTful APIs and web server management",
    "Good communication skills in translating client requirements to technical implementation",
], s_bullet)

story2 += sec("EDUCATION", s_section)
story2.append(Paragraph(
    "<b>BS Computer Science</b>  |  Central Philippine State University, CHMSU  |  2019 - 2023<br/>"
    "Thesis: Web Developing with Java/JSP and MySQL using MVC Pattern", s_body))

story2 += sec("PROJECTS", s_section)
story2.append(Paragraph("<b>Web Developer Portfolio Site (HTML/CSS/JavaScript)</b>", s_body))
story2 += bl([
    "Advanced knowledge of HTML/CSS/JavaScript applied for responsive web developing",
    "Familiar with MVC pattern -- used in organizing web developing codebase",
    "Excellent capability to handle database especially MySQL for portfolio data",
], s_bullet)
story2.append(Spacer(1, 4))
story2.append(Paragraph("<b>MySQL Database Management System (Java/JSP)</b>", s_body))
story2 += bl([
    "Very good knowledge of Java and JSP for server-side web developing and database logic",
    "Excellent capability to handle database especially MySQL -- used for inventory management",
    "Working knowledge of MongoDB integrated alongside MySQL for hybrid data storage solutions",
    "Implementation of security and data protection for database user records",
    "Cross-platform optimization across Internet browsers and operating systems",
], s_bullet)
story2.append(Spacer(1, 4))
story2.append(Paragraph("<b>RESTful API Web Service (HTML/CSS/JavaScript + MySQL)</b>", s_body))
story2 += bl([
    "Fair understanding of building RESTful APIs -- built and deployed a web service",
    "Used web servers and UI/UX design in the development procedure",
    "Good communication skill -- translated complex client requirements to technical implementation",
    "Hardworking and innovative -- delivered results while persisting under pressure",
], s_bullet)

story2 += sec("CERTIFICATIONS", s_section)
story2 += bl([
    "Web Developer Certification -- HTML/CSS/JavaScript (2023)",
    "Java and JSP Server-Side Web Developing (2024)",
    "MySQL Database Management -- Excellent Capability Certification (2024)",
    "RESTful API Design and MVC Pattern (2024)",
], s_bullet)

build_pdf("media/john_coronel_webdev_cv.pdf", story2)

print("Both PDFs generated successfully!")
