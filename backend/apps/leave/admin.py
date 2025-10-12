from django.contrib import admin
from .models import LeaveApplication


@admin.register(LeaveApplication)
class LeaveApplicationAdmin(admin.ModelAdmin):
    list_display = ['get_applicant', 'leave_type', 'start_date', 'end_date', 'total_days', 'status', 'approved_by']
    list_filter = ['leave_type', 'status', 'start_date']
    search_fields = ['reason', 'student__first_name', 'staff__first_name']
    ordering = ['-created_at']

    def get_applicant(self, obj):
        return obj.applicant_name
    get_applicant.short_description = 'Applicant'
