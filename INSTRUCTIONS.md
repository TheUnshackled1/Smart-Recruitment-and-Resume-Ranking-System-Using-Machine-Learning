# Smart Recruitment System — Local Setup (Windows, Python 3.9)

This is the setup that actually runs: Python 3.9 venv, SQLite database,
PDF resume parsing via pdfminer.six. No MySQL/Postgres, no textract.

## 1. Python 3.9
Project requires Python 3.9 (Django 3.2 + pinned ML libs; not 3.11/3.12).
```
py -3.9 --version
```
If missing (Windows):
```
winget install Python.Python.3.9
```

## 2. Create + activate a virtual environment
```
py -3.9 -m venv venv
.\venv\Scripts\activate
```

## 3. Install dependencies
```
pip install -r requirements.txt
```

## 4. Download NLTK data (one time)
```
python -c "import nltk; [nltk.download(p) for p in ['punkt','stopwords','wordnet','omw-1.4']]"
```

## 5. Database (SQLite — no server needed)
Already configured in `JobPortal/settings.py`. Just create the tables:
```
python manage.py migrate
```

## 6. Create a recruiter / admin account
```
python manage.py createsuperuser
```
Roles: `is_staff=True` (or superuser) = **recruiter** (post jobs, rank, approve).
Normal sign-ups via the website = **candidates** (browse + apply only).

## 7. Run
```
python manage.py runserver
```
- App:   http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Notes
- CVs must be **text-based PDF** (scanned/image PDFs extract no text).
- To make an existing user a recruiter: Django admin → Users → tick `is_staff`.
