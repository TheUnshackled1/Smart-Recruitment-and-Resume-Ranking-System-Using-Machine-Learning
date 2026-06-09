---
name: code-review
description: Perform code reviews for the Smart Recruitment System. Use when reviewing PRs, examining changes to Django models, ML ranking logic, access control, or email handling. Covers security, role-based access, performance, ML correctness, and design patterns specific to this project.
---

# Smart Recruitment System Code Review Guide

Follow these guidelines when reviewing code changes for this Django + ML job portal.

## Review Checklist

### Identifying Problems

Look for these issues in code changes:

#### Django & ORM
- **N+1 queries**: Database queries in loops; use `prefetch_related()`, `select_related()`
- **QuerySet mutations**: Calling `.all()` after filters, unnecessary re-queries
- **Model validation**: Missing `clean()` methods, validation only in forms
- **Signals abuse**: Using signals for business logic (use explicit method calls instead)
- **Hardcoded settings**: Environment-dependent values should use `.env` and `settings.py`

#### Role-Based Access Control
- **Missing `@staff_required` guards**: Views must check `user.is_staff` for recruiter-only actions
- **Client-side validation only**: Never trust frontend role checks; always validate in views/models
- **Information leakage**: Candidates shouldn't see recruiter-only fields; filter querysets by role
- **CSRF/CSRF tokens**: All forms receiving POST/PUT/DELETE must have `{% csrf_token %}`

#### ML Ranking Pipeline (screen.py)
- **Text processing assumptions**: Resume text may be malformed, empty, or non-ASCII; add guards
- **PDF extraction errors**: `PyPDF2` can fail on corrupted PDFs; wrap in try/except
- **Vocab mismatches**: TF-IDF vectorizer must not be re-created per ranking; cache it or validate vocabulary
- **Score thresholds**: Hard-coded score cutoffs (0.60, 0.85) must be configurable and tested
- **Empty result sets**: Ranking with 0 candidates or invalid job description should fail gracefully
- **Performance**: Vectorization scales O(n×m) where n=resumes, m=vocab; test with >100 resumes

#### Security
- **SQL injection**: Never use `.raw()` without parameterized queries
- **File upload path traversal**: Validate uploaded CV filenames, store outside web root
- **Email injection**: Sanitize email content before sending via SMTP
- **Exposed secrets**: No API keys, credentials, or database URLs in code; use `.env` only
- **Cross-site scripting (XSS)**: Use `{{ var }}` (auto-escaped) not `{{ var|safe }}` without sanitization

#### Email Handling
- **Missing error handling**: Email failures shouldn't crash the application; use try/except
- **Blocking operations**: Email sending should be async (use Celery or similar if scaling)
- **Template validation**: Email templates must include all required context variables

### Design Assessment

- Does the change fit the existing role-based access pattern (is_staff flag)?
- Does it interact correctly with the ML ranking pipeline or could it introduce stale data?
- Are there side effects on related models (e.g., changing Apply_job status → email notifications)?
- Does it follow Django conventions (models.py, views.py, forms.py structure)?

### Test Coverage

Every PR should have appropriate tests:

- **Model tests**: Business logic, validation rules, role-based queries
- **View tests**: Access control (recruiter vs. candidate), GET/POST/redirect behavior, 403/404 responses
- **Integration tests**: Job posting → application ranking → email notification pipeline
- **ML ranking tests**: Edge cases (empty resumes, 0 candidates, malformed PDFs, invalid vocabulary)

Example test pattern:
```python
def test_recruiter_only_view():
    """Candidate users cannot access recruiter dashboard"""
    candidate = User.objects.create(is_staff=False)
    response = client.get('/recruiter/dashboard/')
    assert response.status_code == 403
```

Avoid excessive branching in tests; focus on actual requirements and edge cases.

### Long-Term Impact

Flag for senior review when changes involve:

- **Schema changes**: Adding/removing fields on PostJob, Apply_job, User models
- **API contracts**: Changing ranking pipeline output format or score interpretation
- **Authentication/Authorization**: Adding new roles or modifying access control
- **ML logic**: Changes to text processing, vectorization, scoring thresholds
- **Email templates**: Changes to notification content sent to users

## Feedback Guidelines

### Tone

- Be polite and empathetic
- Provide actionable suggestions, not vague criticism
- Question assumptions: "Did we test this with PDFs >10MB?" or "Should this be async?"

### Approval

- Approve when only minor issues remain
- Don't block on stylistic preferences (variable names, comment style)
- Remember: the goal is risk reduction, not perfect code

## Common Patterns to Flag

### Django Models & Queries

```python
# ❌ Bad: N+1 query in ranking loop
for application in Apply_job.objects.all():
    print(application.user.username)  # Separate query per user

# ✅ Good: Prefetch user data
applications = Apply_job.objects.select_related('user')
for application in applications:
    print(application.user.username)  # No extra queries
```

```python
# ❌ Bad: No role-based filtering
def get_applications():
    return Apply_job.objects.all()  # Could leak candidate data to other users

# ✅ Good: Filter by role
def get_applications(user):
    if user.is_staff:
        return Apply_job.objects.all()  # Recruiter sees all
    return Apply_job.objects.filter(user=user)  # Candidate sees only their own
```

### Role-Based Access Control

```python
# ❌ Bad: Frontend-only check
def approve_application(request):
    if request.POST.get('user_role') == 'recruiter':  # Client can spoof this!
        # Process approval
        pass

# ✅ Good: Server-side validation
def approve_application(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Only recruiters can approve applications")
    # Process approval
```

### ML Ranking Pipeline

```python
# ❌ Bad: No guards for edge cases
def rank_resumes(job_id):
    job = PostJob.objects.get(id=job_id)
    applications = Apply_job.objects.filter(posted_job=job)
    resumes = [extract_pdf(app.cv) for app in applications]
    vectorizer = TfidfVectorizer()  # New vectorizer each time!
    X = vectorizer.fit_transform([job.description] + resumes)
    return score_resumes(X)

# ✅ Good: Handle edge cases, cache vectorizer
def rank_resumes(job_id):
    try:
        job = PostJob.objects.get(id=job_id)
    except PostJob.DoesNotExist:
        return []

    applications = Apply_job.objects.filter(posted_job=job)
    if not applications.exists():
        return []  # No resumes to rank

    resumes = []
    for app in applications:
        try:
            text = extract_pdf(app.cv)
            if not text.strip():
                continue  # Skip empty resumes
            resumes.append(text)
        except Exception as e:
            logger.error(f"PDF extraction failed for {app.id}: {e}")
            continue

    if not resumes:
        return []  # No valid resumes

    vectorizer = get_or_create_vectorizer(job_id)  # Reuse vectorizer
    X = vectorizer.transform([job.description] + resumes)
    return score_resumes(X)
```

```python
# ❌ Bad: Hard-coded thresholds
score = cosine_distance(...)
if score <= 0.60:
    rank = "STRONG"
elif score <= 0.85:
    rank = "POSSIBLE"
else:
    rank = "WEAK"

# ✅ Good: Configurable thresholds
RANKING_THRESHOLDS = {
    'STRONG': 0.60,
    'POSSIBLE': 0.85,
    'WEAK': float('inf'),
}
rank = get_rank_by_score(score, RANKING_THRESHOLDS)
```

### Email Handling

```python
# ❌ Bad: No error handling
def send_approval_email(application):
    email = Email(
        subject="Your application was approved",
        body=render_email_template('approval', {'app': application}),
        to=application.user.email
    ).send()  # Crashes if email invalid or SMTP fails

# ✅ Good: Graceful error handling
def send_approval_email(application):
    try:
        email = Email(
            subject="Your application was approved",
            body=render_email_template('approval', {'app': application}),
            to=application.user.email
        ).send()
    except SMTPException as e:
        logger.error(f"Failed to send approval email to {application.user.email}: {e}")
        # Optionally queue for retry, but don't crash
    except TemplateDoesNotExist as e:
        logger.error(f"Email template missing: {e}")
```

### Security: File Uploads

```python
# ❌ Bad: Unsanitized filename
def upload_cv(request):
    cv = request.FILES['cv']
    cv.save(f'resumes/{cv.name}')  # Attacker could upload ../../../etc/passwd

# ✅ Good: Validate and sanitize
import os
from django.core.files.storage import default_storage

def upload_cv(request):
    cv = request.FILES['cv']
    # Verify file type and size
    if not cv.name.endswith('.pdf'):
        return HttpResponseBadRequest("Only PDF files allowed")
    if cv.size > 5 * 1024 * 1024:  # 5MB max
        return HttpResponseBadRequest("File too large")

    # Generate safe filename (hash + original extension)
    safe_name = f"{uuid.uuid4().hex}.pdf"
    default_storage.save(f'resumes/{safe_name}', cv)
    # Store safe_name in database, not uploaded name
```

## Project-Specific Considerations

### When Reviewing ML Changes
- Are edge cases covered (empty vocabularies, 0 candidates, malformed text)?
- Is performance tested with realistic data volume (100+ resumes)?
- Are thresholds configurable vs hard-coded?
- Is the vectorizer lifecycle managed correctly (not recreated per call)?

### When Reviewing Access Control Changes
- Does the change respect the two-role model (recruiter vs. candidate)?
- Are querysets filtered by user role?
- Do forms validate user permissions before processing?
- Is there a test that confirms unauthorized users get 403?

### When Reviewing Email Changes
- Are templates validated (no missing context variables)?
- Is error handling in place (SMTP failures, invalid emails)?
- Could email content be injected (use templates, not concatenation)?
- Are notifications semantically correct (status changes, approvals)?

## References

- [Django ORM Performance](https://docs.djangoproject.com/en/3.2/topics/db/optimization/)
- [Django Security](https://docs.djangoproject.com/en/3.2/topics/security/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- Project: [Smart Recruitment System Architecture](./docs/CODE_REVIEW.md)
