# Smart Recruitment System — Local Setup Guide

> **Platform:** Windows · **Python:** 3.9 · **Database:** SQLite · **PDF parsing:** PyPDF2

This guide covers the exact setup that works for this project. Key constraints:
- **Python 3.9 is required** (Django 3.2 and pinned ML libraries are incompatible with Python 3.11/3.12)
- **SQLite only** — no MySQL or PostgreSQL needed
- **Text-based PDF CVs only** — no `.doc`/`.docx` support (textract removed)

---

## Step 1 — Verify Python 3.9

```powershell
py -3.9 --version
```

If Python 3.9 is not installed:
```powershell
winget install Python.Python.3.9
```

---

## Step 2 — Create & Activate a Virtual Environment

```powershell
py -3.9 -m venv venv
.\venv\Scripts\activate
```

Your prompt should now show `(venv)`.

---

## Step 3 — Install Dependencies

```powershell
pip install -r requirements.txt
```

Key packages installed:

| Package | Version | Purpose |
|---|---|---|
| Django | 3.2.25 | Web framework |
| scikit-learn | 1.3.2 | TF-IDF + KNN ranking |
| nltk | 3.8.1 | NLP tokenisation & stemming |
| PyPDF2 | 3.0.1 | PDF text extraction |
| inflect | 5.6.2 | Word inflection |
| stop-words | 2018.7.23 | Stopword lists |

---

## Step 4 — Download NLTK Data *(one-time only)*

```powershell
python -c "import nltk; [nltk.download(p) for p in ['punkt','stopwords','wordnet','omw-1.4']]"
```

This downloads the corpora needed for tokenisation, stop-word removal, and lemmatisation.

---

## Step 5 — Set Up the Database

SQLite is already configured in `JobPortal/settings.py`. Just create the tables:

```powershell
python manage.py migrate
```

No database server installation required.

---

## Step 6 — Create a Recruiter / Admin Account

```powershell
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

**Role mapping:**

| Django flag | Role in the app |
|---|---|
| `is_superuser = True` | Full admin access |
| `is_staff = True` | Recruiter — can post jobs, view rankings, shortlist candidates |
| Neither (default) | Candidate — can browse jobs and apply |

To promote an existing registered user to recruiter:
**Django Admin** (`/admin/`) → **Users** → select the user → tick **`is_staff`** → Save.

---

## Step 7 — Run the Development Server

```powershell
python manage.py runserver
```

| URL | Purpose |
|---|---|
| http://127.0.0.1:8000/ | Main application |
| http://127.0.0.1:8000/admin/ | Django admin panel |

---

## Notes & Known Constraints

| Topic | Detail |
|---|---|
| **CV format** | Must be a **text-based PDF**. Scanned / image PDFs will extract no text and receive a zero match score. |
| **Python version** | Only Python 3.9 is supported. Do not use 3.10, 3.11, or 3.12. |
| **Database** | SQLite only (configured in `JobPortal/settings.py`). MySQL/PostgreSQL not supported in this setup. |
| **File types** | PDF only. `.doc` / `.docx` support has been removed (textract dependency removed). |
| **NLTK data** | Must be downloaded once per machine (Step 4). If the server throws an NLTK `LookupError`, re-run Step 4. |
