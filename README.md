Smart Recruitment and Resume Ranking System Using Machine Learning

Finding the most suitable candidate for a job vacancy within a short period of time has become a major challenge for many companies. With the increasing number of job applicants, the recruitment process requires significant time, effort, and manpower to manually review resumes and identify qualified candidates. Human Resource personnel often face difficulties in efficiently screening large volumes of applications.

This project aims to develop a Smart Recruitment and Resume Ranking System Using Machine Learning, a web-based application built with Django that automates the recruitment and applicant screening process. In this system, recruiter users can post job vacancies, while applicant users can apply for jobs, provide the required information, and upload their resumes.

The system analyzes and compares the uploaded resumes with the job descriptions using document similarity techniques and a K-Nearest Neighbors (KNN) machine learning model. Based on the similarity scores, the system automatically ranks and shortlists the most qualified candidates for the position.

By automating the resume screening and ranking process, the system helps reduce manual effort, saves time and operational costs, and improves the efficiency and accuracy of candidate selection for recruitment.

## Objectives

I've designed this system with four key goals in mind:

**Find the Best Candidates** — My system identifies the most qualified applicants for each job vacancy, ensuring you get the right talent for your team.

**Provide a Realistic Ranking System** — I implement an intelligent algorithm that scores candidates based on their actual skills and real-world experience, not just keyword matches.

**Make the Recruiting Process More Flexible** — I support multiple data sources including CV uploads, GitHub profiles, and LinkedIn profiles to get a complete picture of each candidate.

**Save Human Efforts, Time, and Cost** — By automating the screening and ranking process, I significantly reduce the manual effort required from your HR team, saving both time and operational costs.

## Setup & Dependencies

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- SQLite3

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Smart-Recruitment-System
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # or
   source venv/bin/activate     # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://localhost:8000/`

### Database
The system uses SQLite for local development, which is automatically configured in Django settings.

## Core Features

### For Recruiters

Recruiters can easily post job vacancies and create detailed job listings with specific requirements, skills, and experience levels they're looking for. Once candidates start applying, recruiters can access and review all submissions in one convenient dashboard. My system automatically ranks candidates based on CV matching and required skills, making it easy to spot the best fits. Finally, recruiters can review my shortlisted and matched candidates for interview rounds.

### For Candidates/Applicants

Job seekers can browse available positions and filter by location, salary, and employment type to find opportunities that match their goals. They can submit applications along with their CV and cover letter. To provide a more complete profile, candidates can link their GitHub and LinkedIn profiles to showcase their work and experience. Additionally, candidates can participate in assessments for positions they've applied to.

### System Capabilities

The system extracts information from multiple sources: uploaded CVs, GitHub profiles, and LinkedIn profiles. It automatically identifies and matches skills from candidate profiles with what the job requires. Using TF-IDF and K-Nearest Neighbors algorithms, my intelligent ranking system scores and ranks candidates fairly. The system also automates the filtering process based on academic qualifications, experience level, and required skills.

## System Architecture

The Smart Recruitment System follows a layered architecture with the following main components:

### Overall System Flow

```
Candidates → Job Search, Apply Job, Upload CV, Participate Assessment
                              ↓
                    System CVs Database
                              ↓
                   CV Ranking System
                   (Parsing & Analysis)
                              ↓
                    Shortlisted CVs
```

### CV Ranking Model Architecture

The ranking system processes candidate information through a well-designed pipeline that ensures accurate and fair candidate evaluation.

The system accepts data from three main sources: CV uploads, GitHub profiles, and LinkedIn profiles. This multi-source approach gives me a comprehensive view of each candidate's qualifications.

**Processing Pipeline:**

The system begins by parsing and extracting information from CVs, GitHub profiles, and LinkedIn profiles. Next, it cleans the extracted data by removing special characters, signal letters, and numbers to standardize the text.

Using NLTK tokenization, the cleaned text is converted into meaningful tokens. I then prepare the data further by removing stop words and applying word stemming to normalize variations of the same word.

For requirement extraction, I use TF-IDF analysis to identify which words are most relevant and important. These keywords are then mapped back to each CV based on the specific job requirements.

The system then calculates matching similarity scores to identify which CVs are most compatible with the job vacancy, focusing on required skills. Using my ranking algorithm, I generate a ranked list of the top matching CVs (for example, the top 20 candidates).

Finally, I calculate a final score that combines both the CV matching score and the assessment results, giving recruiters a comprehensive view of each candidate's suitability for the role.

### Ranking Algorithm Design

**Basic Requirements Filtering**

Before I even start ranking, I ensure candidates meet the fundamental requirements. I filter based on academic CGPA or degree qualifications and minimum required years of experience. This ensures I'm working with qualified candidates from the start.

**Data Pre-processing**

My system cleans and standardizes the candidate data through data cleaning (removing special characters, signals, and numbers), word stemming, and verb lemmatization. This normalization step ensures consistent comparison across all resumes.

**TF-IDF Calculation**

I use TF-IDF (Term Frequency-Inverse Document Frequency) to understand which keywords are most important in matching a candidate to a job. The calculation works as follows:

- TF(keyword) measures how often a keyword appears in a resume
- IDF(keyword) measures how unique that keyword is across all resumes. For required skills, I set IDF to 1, and for unwanted skills, I set it to 0
- weight(keyword) = TF(keyword) × IDF(keyword), giving me a final importance score for each keyword

**Document Similarity Matching**

I use the TF-IDF weighted vectors and apply the K-Nearest Neighbors (KNN) algorithm to find candidates most similar to the job requirements. This involves calculating cosine similarity between each CV and the job description to find the best matches.

**Final Scoring**

The final score combines the candidate's skill matching score with their assessment performance. I then rank all candidates based on this final score and return the top K candidates (typically the top 20) as my recommendations to the recruiter.