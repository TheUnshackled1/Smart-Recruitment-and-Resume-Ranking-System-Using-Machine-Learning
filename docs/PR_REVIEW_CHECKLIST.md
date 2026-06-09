---
name: PR Review Checklist
description: Use this checklist when reviewing pull requests for Smart Recruitment System. Follows CODE_REVIEW.md guidelines.
---

# PR Review Checklist

## Before You Start
- [ ] PR title is clear and concise (under 70 chars)
- [ ] PR description explains **why** not just **what**
- [ ] Code changes are focused (not mixing features + refactoring)
- [ ] All tests pass locally (`python manage.py test`)

---

## Role-Based Access Control ⚠️ CRITICAL

- [ ] No new recruiter-only views missing `@staff_required` decorator
- [ ] If accessing single job/application: checks ownership (`if obj.user != request.user`)
- [ ] QuerySets filtered by role (recruiters see all; candidates see only theirs)
- [ ] No `is_staff` checks on frontend only (all validation server-side)
- [ ] Test added: "Candidate cannot access recruiter view" returns 403

**Action Items:**
- [ ] Link to: `CODE_REVIEW.md` Role-Based Access Control section

---

## Database & Query Performance 📊

- [ ] No `.get_queryset()` after `.filter()` (redundant chaining)
- [ ] No queries in loops (check for N+1 patterns)
- [ ] Related objects use `select_related()` (ForeignKey) or `prefetch_related()` (ManyToMany)
- [ ] `values()` / `annotate()` queries are separate (not re-running per item)
- [ ] No `count()` on querysets used later (combine with first query)

**Example N+1 to flag:**
```python
for app in Apply_job.objects.all():
    print(app.user.username)  # ❌ Query per user
```

**Action Items:**
- [ ] Link to: `CODE_REVIEW.md` Django & ORM section

---

## ML Ranking Pipeline 🤖

### If changes touch `screen.py` or ranking logic:

- [ ] PDF extraction wrapped in try/except (handles corrupted files)
- [ ] Empty resume list handled gracefully (returns empty dict, not crash)
- [ ] Text normalization failures caught (empty tokens → handled as empty string)
- [ ] TF-IDF vectorizer handles empty vocabulary (catches ValueError)
- [ ] Hard-coded thresholds (0.60, 0.85) are configurable settings or constants
- [ ] Test with realistic edge cases (empty PDF, non-ASCII text, no keywords)

**Real-World Test:**
```python
# Should not crash with these inputs:
- PDF with no text
- Resume with only emojis/special chars
- Job description with no keywords after normalization
- Zero candidates
```

**Action Items:**
- [ ] Link to: `CODE_REVIEW.md` ML Ranking Pipeline section

---

## Security 🔒 BLOCK IF ISSUES

### File Uploads
- [ ] File type validated (only .pdf allowed, not `.exe`, `.py`, etc.)
- [ ] File size limited (reject >5MB)
- [ ] Filename sanitized (no `../` path traversal)
- [ ] Files stored outside web root (Django default: `MEDIA_ROOT`)
- [ ] Test: "Uploading .zip file rejected"

### Email
- [ ] Email content uses Django templates (not string concatenation)
- [ ] All template variables checked to exist before rendering
- [ ] Email failures handled gracefully (try/except, don't crash app)
- [ ] No secrets/tokens in email body
- [ ] Test: "Sending to invalid email doesn't crash"

### Data Validation
- [ ] Form validation in `forms.py` (not just views)
- [ ] Database constraints (NOT NULL, UNIQUE, etc.) documented
- [ ] User input escaped/sanitized before display (`{{ var }}` not `{{ var|safe }}`)
- [ ] SQL injection risks checked (use ORM, no `.raw()` without params)

**Action Items:**
- [ ] Link to: `CODE_REVIEW.md` Security section

---

## Contact Form & Notifications 📧

- [ ] Contact form submission saved to database
- [ ] Confirmation email sent to submitter
- [ ] Admin notification sent (all recruiters or specific recipient)
- [ ] Failed emails logged (not silently ignored)
- [ ] Template checks: all required fields present

**Action Items:**
- [ ] Link to: `CODE_REVIEW.md` Email Handling section

---

## Documentation & Code Quality 📝

- [ ] Comments explain **why**, not **what** (self-documenting code)
- [ ] Function names are clear (verb-noun: `get_applications()` not `data()`)
- [ ] No dead code or commented-out blocks (remove or explain)
- [ ] Magic numbers extracted to constants (e.g., `PAGINATION_SIZE = 10`)
- [ ] No print() statements left in production code (use logging)

---

## Testing 🧪

- [ ] New models have tests for `__str__()`, `clean()`, business logic
- [ ] New views have tests for:
  - Authenticated vs. unauthenticated access
  - Recruiter vs. candidate authorization (403 responses)
  - Form validation (missing fields, invalid data)
  - Edge cases (empty queryset, missing object)
- [ ] ML ranking tests include edge cases (empty resumes, invalid text)
- [ ] Email tests verify content and recipient

**Minimum test template:**
```python
def test_recruiter_can_access_ranking(self):
    recruiter = User.objects.create(is_staff=True)
    job = PostJob.objects.create(user=recruiter, ...)
    response = client.get(f'/ranking/{job.id}/')
    assert response.status_code == 200

def test_candidate_cannot_access_ranking(self):
    recruiter = User.objects.create(is_staff=True)
    job = PostJob.objects.create(user=recruiter, ...)
    candidate = User.objects.create(is_staff=False)
    client.login(username=candidate.username, password='test')
    response = client.get(f'/ranking/{job.id}/')
    assert response.status_code == 403
```

---

## Merge Decision

### ✅ APPROVE If:
- [ ] All critical checks passed (RBAC, Security, ML edge cases)
- [ ] Tests show good coverage
- [ ] Code follows project patterns
- [ ] Only minor issues remain

### ⏸️ REQUEST CHANGES If:
- [ ] Missing `@staff_required` on recruiter-only views
- [ ] File upload lacks validation
- [ ] SQL injection risk detected
- [ ] N+1 query created
- [ ] Email failures not handled
- [ ] Hard-coded values should be configurable

### ❌ BLOCK If:
- [ ] Security vulnerability (XSS, path traversal, injection)
- [ ] Breaking change without migration plan
- [ ] Breaks existing tests

---

## Feedback Template

```markdown
### 🎯 Summary
[Brief description of the changes]

### ✅ Looks Good
- [Positive observation]

### 🔍 Questions
- [Clarifications needed]

### 🚨 Changes Needed
- [Issue]: [Description]. See CODE_REVIEW.md line X.
  Suggestion: [How to fix]

### 💭 Nice-to-Have (Optional)
- [Polish suggestions]
```

---

## Links

- **[CODE_REVIEW.md](./CODE_REVIEW.md)** — Full review guidelines
- **[Architecture](./architecture.md)** — System design overview
- **[Local Setup](./local-dev-setup.md)** — Dev environment instructions
- **[Test Report](./CODE_REVIEW_TEST_REPORT.md)** — Real issues caught by this guide
