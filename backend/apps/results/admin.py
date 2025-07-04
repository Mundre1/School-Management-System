from django.contrib import admin
from .models import Exam, Subject, Result


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['name', 'exam_type', 'grade', 'academic_year', 'start_date', 'end_date']
    list_filter = ['exam_type', 'grade', 'academic_year']
    search_fields = ['name']
    ordering = ['-start_date']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'grade']
    list_filter = ['grade']
    search_fields = ['name', 'code']
    ordering = ['grade', 'name']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'exam', 'subject', 'marks_obtained', 'total_marks', 'percentage', 'grade']
    list_filter = ['exam', 'subject', 'grade']
    search_fields = ['student__first_name', 'student__last_name']
    ordering = ['-created_at']
