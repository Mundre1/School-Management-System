from django.contrib import admin
from .models import ClassRoom, Subject, Period, Timetable


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade', 'section', 'capacity', 'class_teacher', 'is_active']
    list_filter = ['grade', 'is_active']
    search_fields = ['name', 'room_number']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'grade', 'is_compulsory', 'is_active']
    list_filter = ['grade', 'is_compulsory', 'is_active']
    search_fields = ['name', 'code']


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ['period_number', 'start_time', 'end_time', 'is_break', 'break_name']
    list_filter = ['is_break']
    ordering = ['period_number']


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ['classroom', 'day', 'period', 'subject', 'teacher', 'is_active']
    list_filter = ['day', 'classroom', 'is_active']
    search_fields = ['classroom__name', 'subject__name', 'teacher__first_name']
    ordering = ['day', 'period__period_number']
