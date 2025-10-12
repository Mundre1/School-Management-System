from django.contrib import admin
from .models import Assignment, AssignmentSubmission


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'classroom', 'subject', 'teacher', 'due_date', 'total_marks', 'status']
    list_filter = ['status', 'classroom', 'subject', 'due_date']
    search_fields = ['title', 'description']
    ordering = ['-created_at']


@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'student', 'status', 'marks_obtained', 'submitted_at', 'graded_at']
    list_filter = ['status', 'submitted_at', 'graded_at']
    search_fields = ['assignment__title', 'student__first_name', 'student__last_name']
    ordering = ['-submitted_at']
