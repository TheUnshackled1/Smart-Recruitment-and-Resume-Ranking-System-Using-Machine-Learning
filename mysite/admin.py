from django.contrib import admin
from mysite.models import Contact
from mysite.models import PostJob
from mysite.models import Apply_job


@admin.register(Apply_job)
class ApplyJobAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'experience', 'company_name', 'title', 'status', 'start_date', 'start_location', 'cv')
    list_editable = ('status',)
    list_filter = ('status', 'company_name', 'title', 'gender')
    search_fields = ('name', 'email', 'company_name', 'title')
    actions = ('approve_selected', 'reject_selected', 'reset_to_pending')

    @admin.action(description='Approve selected applicants')
    def approve_selected(self, request, queryset):
        updated = queryset.update(status='Approved')
        self.message_user(request, f'{updated} applicant(s) approved.')

    @admin.action(description='Reject selected applicants')
    def reject_selected(self, request, queryset):
        updated = queryset.update(status='Rejected')
        self.message_user(request, f'{updated} applicant(s) rejected.')

    @admin.action(description='Reset selected to Pending')
    def reset_to_pending(self, request, queryset):
        updated = queryset.update(status='Pending')
        self.message_user(request, f'{updated} applicant(s) reset to Pending.')


@admin.register(PostJob)
class PostJobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'employment_status', 'gender',
                    'vacancy', 'job_location', 'application_deadline')
    list_filter = ('company_name', 'employment_status', 'gender')
    search_fields = ('title', 'company_name', 'job_location')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject')
    search_fields = ('name', 'email', 'subject')
