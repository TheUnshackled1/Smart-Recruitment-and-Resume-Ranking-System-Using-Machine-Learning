import os
try:
    from fpdf import FPDF
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fpdf"])
    from fpdf import FPDF

def create_pdf(filename, text_content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Split text by lines and write
    for line in text_content.split('\n'):
        # handle unicode by replacing characters that might crash fpdf
        line = line.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 10, txt=line)
    
    pdf.output(filename)

strong_sys_analyst = """John Developer
Talisay, Negros Occidental | john.developer@email.com | 0912-345-6789

OBJECTIVE
Highly analytical and detail-oriented IT professional seeking a Systems Analyst position to leverage my experience in system evaluation, requirements gathering, and technical documentation to improve business processes.

EXPERIENCE
Junior Systems Analyst | Tech Innovators (2024 - 2026)
- Evaluated existing IT systems and recommended improvements, increasing efficiency by 15%.
- Gathered and documented user requirements for 5 major software projects.
- Collaborated with software developers to design and implement new system features.
- Conducted system testing, validation, and deployed software updates.
- Trained over 50 end-users on newly implemented systems.

IT Support Specialist | Global Solutions (2023 - 2024)
- Provided technical support and troubleshooting for internal business systems.
- Assisted in the documentation of IT infrastructure.

EDUCATION
Bachelor of Science in Information Technology
CHMSU, Talisay Campus (Graduated 2023)

SKILLS
- System Analysis & Design
- Requirements Gathering & Documentation
- Software Testing & Validation
- SQL, Python, UML
- Cross-functional Collaboration"""

weak_sys_analyst = """Jane Smith
Bacolod City | jane.smith@email.com | 0998-765-4321

OBJECTIVE
Looking for a full-time job to earn a living and learn new things in a friendly environment.

EXPERIENCE
Sales Assistant | Fashion Boutique (2025 - 2026)
- Welcomed customers and helped them find clothes.
- Handled cash register and processed payments.
- Arranged store displays and maintained cleanliness.

Delivery Rider | FastFood Chain (2024 - 2025)
- Delivered food to customers within the specified time.
- Maintained motorcycle in good condition.

EDUCATION
High School Graduate
Bacolod National High School (Graduated 2024)

SKILLS
- Customer Service
- Fast Learner
- Hardworking
- Driving"""

strong_proj_manager = """Alice Manager
Talisay, Negros Occidental | alice.manager@email.com | 0911-222-3333

OBJECTIVE
Experienced Project Manager looking for a new challenge.

EXPERIENCE
Project Manager | TechNova (2020 - 2026)
- Managed cross-functional teams of 20+ members.
- Delivered 15+ software projects on time and within budget.
- Managed risks and resolved conflicts.
- Facilitated agile ceremonies (Scrum Master certified).

Business Analyst | BizTech (2018 - 2020)
- Analyzed business needs and documented requirements.

EDUCATION
Master of Business Administration (MBA)
CHMSU (Graduated 2018)

SKILLS
- Agile & Scrum
- Budgeting & Scheduling
- Risk Management
- Jira & Confluence
"""

weak_proj_manager = """Bob Johnson
Bacolod City | bob.johnson@email.com | 0922-333-4444

OBJECTIVE
Looking for a job.

EXPERIENCE
Cashier | Supermarket (2024 - 2026)
- Processed payments.

Stock Clerk | Warehouse (2023 - 2024)
- Organized items.

EDUCATION
High School Graduate (2023)

SKILLS
- Punctual
- Team player
"""

out_dir = r"c:\Users\jtcor\Documents\OOP\Smart-Recruitment-System\media"
os.makedirs(out_dir, exist_ok=True)

create_pdf(os.path.join(out_dir, "john_developer_strong_systems_analyst.pdf"), strong_sys_analyst)
create_pdf(os.path.join(out_dir, "jane_smith_weak_systems_analyst.pdf"), weak_sys_analyst)
create_pdf(os.path.join(out_dir, "alice_manager_strong_project_manager.pdf"), strong_proj_manager)
create_pdf(os.path.join(out_dir, "bob_johnson_weak_project_manager.pdf"), weak_proj_manager)

print("PDFs generated successfully in media folder.")
