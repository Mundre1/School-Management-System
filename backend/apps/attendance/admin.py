from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'date', 'status', 'marked_by', 'marked_at']
    list_filter = ['status', 'date']
    search_fields = ['student__first_name', 'student__last_name']
    ordering = ['-date']
    date_hierarchy = 'date'
