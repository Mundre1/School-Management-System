from django.contrib import admin
from .models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'first_name', 'last_name', 'department', 'designation', 'status', 'joining_date']
    list_filter = ['department', 'status', 'designation']
    search_fields = ['first_name', 'last_name', 'email', 'employee_id']
    ordering = ['-created_at']
