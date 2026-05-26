from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from mysite import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.db.models import Count

from mysite.models import Contact
from mysite.models import PostJob
from mysite.models import Apply_job
import mysite.screen as screen
import re
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.mail import send_mail
from django.conf import settings


# Recruiter-only gate: must be logged in AND a staff user.
# Candidates (registered with Applicant) have is_staff=False -> redirected.
def staff_required(view_func):
    @wraps(view_func)
    @login_required(login_url='login')
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_staff:
            messages.info(request, 'Only recruiters can access that page.')
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return _wrapped


# write your code
def index(request):
    job_list = PostJob.objects.get_queryset().order_by('id')
    total_jobs = job_list.count()
    total_users = User.objects.all().count()
    total_companies = PostJob.objects.values('company_name').annotate(Count('company_name', distinct=True))
    query_num = 5
    paginator = Paginator(job_list, query_num)
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)
    if qs.has_previous():
        page_show_min = (qs.previous_page_number() - 1) * query_num + 1
    elif total_jobs > 0:
        page_show_min = 1
    else:
        page_show_min = 0
    if qs.has_next():
        page_show_max = (qs.previous_page_number() + 1) * query_num - 1
    else:
        page_show_max = total_jobs
    context = {
        'query': qs,
        'job_listings': job_list,
        'job_len': total_jobs,
        'curr_page1': page_show_min,
        'curr_page2': page_show_max,
        'companies': total_companies.count(),
        'candidates': total_users
    }
    return render(request, "mysite/index.html", context=context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print("user: ", username)
        # print("password: ", password)
        user = auth.authenticate(username=username, password=password)
        if user:
            print(user.is_active, user.is_staff)
        if user is not None:
            auth.login(request, user)
            print(user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'mysite/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        userType = request.POST['user_type']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # phone = request.POST['phone']
        # address = request.POST['address']
        # linkedin_id = request.POST['linkedin_id']
        # github_id = request.POST['github_id']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email, is_staff=(userType == '1'), password=password1)
                user.save()
                # print("username: ", user)
                # print("password: ", password1)
                messages.info(request, 'User Created!')
                return redirect('login')
        else:
            messages.info(request, 'Password is not matching!')
            return redirect('register')
        # return redirect('index')

    else:
        return render(request, 'mysite/register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def about(request):
    return render(request, 'mysite/about.html')


@login_required(login_url='login')
def job_single(request, id):
    job_query = PostJob.objects.get(id=id)
    context = {
        'q': job_query,
    }
    return render(request, "mysite/job-single.html", context)


def job_listings(request):
    job_list = PostJob.objects.get_queryset().order_by('id')
    total_jobs = job_list.count()
    total_users = User.objects.all().count()
    total_companies = PostJob.objects.values('company_name').annotate(Count('company_name', distinct=True))
    query_num = 7
    paginator = Paginator(job_list, query_num)
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)
    if qs.has_previous():
        page_show_min = (qs.previous_page_number() - 1) * query_num + 1
    elif total_jobs > 0:
        page_show_min = 1
    else:
        page_show_min = 0
    if qs.has_next():
        page_show_max = (qs.previous_page_number() + 1) * query_num - 1
    else:
        page_show_max = total_jobs
    context = {
        'query': qs,
        'job_listings': job_list,
        'job_len': total_jobs,
        'curr_page1': page_show_min,
        'curr_page2': page_show_max,
        'companies': total_companies.count,
        'candidates': total_users
    }
    return render(request, "mysite/job-listings.html", context=context)


@staff_required
def post_job(request):
    if request.method == "POST":
        title = request.POST['title']
        company_name = request.POST['company_name']
        employment_status = request.POST['employment_status']
        vacancy = request.POST['vacancy']
        gender = request.POST['gender']
        if 'details' in request.POST:
            details = request.POST['details']
        else:
            details = False
        # details = request.POST.get['details', False]
        if 'responsibilities' in request.POST:
            responsibilities = request.POST['responsibilities']
        else:
            responsibilities = False
        # responsibilities = request.POST['responsibilities']
        experience = request.POST['experience']
        other_benefits = request.POST['other_benefits']
        job_location = request.POST['job_location']
        salary = request.POST['salary']
        application_deadline = request.POST['application_deadline']
        job = PostJob.objects.filter(title=title, company_name=company_name, employment_status=employment_status)
        print(job)
        if not job:
            ins = PostJob(title=title, company_name=company_name, employment_status=employment_status, vacancy=vacancy,
                          gender=gender, details=details,
                          responsibilities=responsibilities, experience=experience, other_benefits=other_benefits,
                          job_location=job_location, salary=salary, application_deadline=application_deadline)
            ins.save()
            messages.info(request, 'Job successfully posted!')

            # storing job description
            # jobfilepath = 'jobDetails/'
            # job_desc = details + '\n' + responsibilities + '\n' + experience + '\n';
            # with open(jobfilepath + company_name + '_' + title + '.txt', 'w+') as file:
            #     file.write(re.sub(' +', ' ', job_desc))
            print("The data has been added into database!")
        else:
            messages.info(request, 'This job is already posted!')
            print('This job is already posted!')
        return redirect('job-listings')
    return render(request, 'mysite/post-job.html', {})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        # phone = request.POST['phone']
        if 'phone' in request.POST:
            phone = request.POST['phone']
        else:
            phone = False

        if 'subject' in request.POST:
            subject = request.POST['subject']
        else:
            subject = False

        if 'desc' in request.POST:
            desc = request.POST['desc']
        else:
            desc = False

        # desc = request.POST['desc']
        # print(name, email, phone, subject, desc)
        ins = Contact(name=name, email=email, phone=phone, subject=subject, desc=desc)
        ins.save()
        print("Data has been save in database!")

        # (b) deliver contact message to admin inbox (console backend in dev)
        try:
            send_mail(
                'Contact form: ' + str(subject),
                'From: ' + name + ' <' + email + '>  phone: ' + str(phone) + '\n\n' + str(desc),
                settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL], fail_silently=True)
        except Exception as e:
            print('email error:', e)

        return redirect('/')

    else:
        return render(request, "mysite/contact.html")


@login_required(login_url='login')
def applyjob(request, id):
    # recruiters (is_staff) cannot apply to jobs
    if request.user.is_staff:
        messages.info(request, "Recruiters can't apply to jobs.")
        return redirect('job-listings')
    job = PostJob.objects.get(id=id)
    print(job.id)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        print(name, email)
        gender = request.POST['gender']
        experience = request.POST['experience']
        print(experience)

        coverletter = request.POST['coverletter']
        cv = request.FILES['cv']
        print(cv)
        print(cv)
        Apply_job.objects.filter(name=name, email__exact=email, company_name=job.company_name, title=job.title).delete()
        ins = Apply_job(name=name, email=email, cv=cv, experience=experience,coverletter=coverletter, company_name=job.company_name, gender=gender,
                            title=job.title)
        ins.save()
        messages.info(request, 'Successfully applied for the post!')
        print("The Data is saved into database!")

        # email notifications (console backend in dev)
        try:
            # (a) confirmation to candidate
            send_mail(
                'Application received - ' + job.title,
                'Hi ' + name + ',\n\nWe received your application for "' + job.title +
                '" at ' + job.company_name + '.\nWe will contact you about next steps.\n\n- Smart Recruitment',
                settings.DEFAULT_FROM_EMAIL, [email], fail_silently=True)
            # (c) alert all recruiters (staff users)
            recruiter_emails = list(
                User.objects.filter(is_staff=True, is_active=True)
                .exclude(email='').values_list('email', flat=True))
            if recruiter_emails:
                send_mail(
                    'New application: ' + job.title,
                    name + ' (' + email + ') applied for "' + job.title + '" at ' +
                    job.company_name + '. Experience: ' + str(experience) + ' yr(s).',
                    settings.DEFAULT_FROM_EMAIL, recruiter_emails, fail_silently=True)
        except Exception as e:
            print('email error:', e)

        return redirect('job-listings')

    return render(request, 'mysite/applyjob.html', {'company_name': job.company_name, 'title': job.title})


# @login_required
# def ranking(request, id):
#     job_query = PostJob.objects.get(id=id)
#     print(job_query.id, job_query.title, job_query.company_name)
#     jobfilename = job_query.company_name + '_' + job_query.title + '.txt'
#     job_desc = job_query.details + '\n' + job_query.responsibilities + '\n' + job_query.experience + '\n';
#     resumes_name = Apply_job.objects.filter(company_name=job_query.company_name, title=job_query.title,
#                                             cv__isnull=False)
#     resumes = [str(item.cv) for item in resumes_name]
#     resumes_new = [item.split(':')[0] for item in resumes]
#     resumes_new = [item for item in resumes_new if item != '']
#     result_arr = screen.res(jobfilename=jobfilename, job_desc=re.sub(r' +', ' ', job_desc.replace('\n', '').replace('\r', '')), list_of_resumes=resumes_new)
#     return render(request, 'mysite/ranking.html',
#                   {'items': result_arr, 'company_name': job_query.company_name, 'title': job_query.title})

def _verdict(score):
    # KNN-score = cosine distance (0..2). Lower = closer match.
    if score <= 0.6:
        return ('Strong match', 'success')
    if score <= 0.85:
        return ('Possible', 'warning')
    return ('Weak / off-topic', 'danger')


@staff_required
def ranking(request, id):
    job_data = PostJob.objects.get(id=id)
    print(job_data.id, job_data.title, job_data.company_name)
    resumes_data = Apply_job.objects.filter(company_name=job_data.company_name, title=job_data.title,
                                            cv__isnull=False)
    result_arr = screen.res(resumes_data, job_data)

    # enrich each ranked item with its Apply_job row + a verdict hint so the
    # template can show CV link, status, Approve/Reject buttons.
    applicants_by_cv = {str(a.cv): a for a in resumes_data}
    items = []
    for _, item in result_arr.items():
        applicant = applicants_by_cv.get(item['name'])
        v_label, v_level = _verdict(item['score'])
        items.append({
            'rank': item['rank'],
            'name': item['name'],
            'score': item['score'],
            'applicant': applicant,
            'verdict_label': v_label,
            'verdict_level': v_level,
        })

    return render(request, 'mysite/ranking.html',
                  {'items': items, 'job': job_data,
                   'company_name': job_data.company_name, 'title': job_data.title})


@staff_required
def set_status(request, id, status):
    app = get_object_or_404(Apply_job, id=id)
    if request.method == 'POST' and status in ('Approved', 'Rejected', 'Pending'):
        app.status = status
        app.save()
        # notify candidate
        verb_map = {'Approved': 'approved', 'Rejected': 'not selected', 'Pending': 'set back to pending'}
        try:
            send_mail(
                'Application status update: ' + app.title,
                'Hi ' + app.name + ',\n\nYour application for "' + app.title + '" at ' +
                app.company_name + ' has been ' + verb_map[status] + '.\n\n- Smart Recruitment',
                settings.DEFAULT_FROM_EMAIL, [app.email], fail_silently=True)
        except Exception as e:
            print('email error:', e)
        messages.info(request, app.name + ' marked ' + status + '.')
    job = PostJob.objects.filter(company_name=app.company_name, title=app.title).first()
    if job:
        return redirect('ranking', id=job.id)
    return redirect('job-listings')


class SearchView(ListView):
    model = PostJob
    template_name = 'mysite/search.html'
    context_object_name = 'all_job'

    def get_queryset(self):
        return self.model.objects.filter(title__contains=self.request.GET['title'],
                                         job_location__contains=self.request.GET['job_location'],
                                         employment_status__contains=self.request.GET['employment_status'])

