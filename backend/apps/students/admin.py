"""
Student Admin Configuration
Professional admin interface for student management
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import Student, Guardian, StudentDocument, StudentNote, StudentAchievement


class GuardianInline(admin.TabularInline):
    """Inline admin for guardians"""
    model = Guardian
    extra = 0
    fields = ('name', 'relation', 'phone', 'email', 'is_primary', 'is_emergency_contact')


class StudentDocumentInline(admin.TabularInline):
    """Inline admin for student documents"""
    model = StudentDocument
    extra = 0
    fields = ('document_type', 'document_name', 'document_file', 'uploaded_at')
    readonly_fields = ('uploaded_at',)


class StudentNoteInline(admin.StackedInline):
    """Inline admin for student notes"""
    model = StudentNote
    extra = 0
    fields = ('note_type', 'title', 'content', 'is_private')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Admin interface for Student model"""
    
    list_display = (
        'admission_number', 'get_student_name', 'class_name', 'section',
        'status', 'admission_date', 'get_age'
    )
    list_filter = ('status', 'class_name', 'section', 'admission_type', 'academic_year')
    search_fields = (
        'admission_number', 'roll_number', 'user__first_name',
        'user__last_name', 'user__email', 'father_name', 'mother_name'
    )
    readonly_fields = ('id', 'created_at', 'updated_at', 'get_age')
    
    fieldsets = (
        ('User Account', {
            'fields': ('user',)
        }),
        ('Academic Information', {
            'fields': (
                'admission_number', 'roll_number', 'class_name', 'section',
                'academic_year', 'status'
            )
        }),
        ('Admission Details', {
            'fields': ('admission_date', 'admission_type', 'previous_school')
        }),
        ('Father Information', {
            'fields': ('father_name', 'father_phone', 'father_email', 'father_occupation')
        }),
        ('Mother Information', {
            'fields': ('mother_name', 'mother_phone', 'mother_email', 'mother_occupation')
        }),
        ('Medical Information', {
            'fields': ('medical_conditions', 'allergies'),
            'classes': ('collapse',)
        }),
        ('Documents', {
            'fields': ('birth_certificate', 'transfer_certificate'),
            'classes': ('collapse',)
        }),
        ('System Information', {
            'fields': ('id', 'created_at', 'updated_at', 'get_age'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [GuardianInline, StudentDocumentInline, StudentNoteInline]
    
    def get_student_name(self, obj):
        """Display student full name"""
        return obj.user.get_full_name()
    get_student_name.short_description = 'Student Name'
    
    def get_age(self, obj):
        """Display student age"""
        return f"{obj.age} years" if obj.age else "N/A"
    get_age.short_description = 'Age'
    
    def get_queryset(self, request):
        """Optimize queryset with select_related"""
        return super().get_queryset(request).select_related('user')


@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    """Admin interface for Guardian model"""
    
    list_display = ('name', 'relation', 'get_student_name', 'phone', 'is_primary', 'is_emergency_contact')
    list_filter = ('relation', 'is_primary', 'is_emergency_contact')
    search_fields = ('name', 'phone', 'email', 'student__user__first_name', 'student__user__last_name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Student', {
            'fields': ('student',)
        }),
        ('Guardian Information', {
            'fields': ('name', 'relation', 'phone', 'email', 'occupation', 'address')
        }),
        ('Priority', {
            'fields': ('is_primary', 'is_emergency_contact')
        }),
        ('System Information', {
            'fields': ('id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_student_name(self, obj):
        """Display student name"""
        return obj.student.user.get_full_name()
    get_student_name.short_description = 'Student'


@admin.register(StudentDocument)
class StudentDocumentAdmin(admin.ModelAdmin):
    """Admin interface for Student Document model"""
    
    list_display = ('document_name', 'document_type', 'get_student_name', 'uploaded_by', 'uploaded_at')
    list_filter = ('document_type', 'uploaded_at')
    search_fields = ('document_name', 'student__user__first_name', 'student__user__last_name')
    readonly_fields = ('id', 'uploaded_at', 'updated_at')
    
    fieldsets = (
        ('Student', {
            'fields': ('student',)
        }),
        ('Document Information', {
            'fields': ('document_type', 'document_name', 'document_file', 'description')
        }),
        ('Upload Information', {
            'fields': ('uploaded_by',)
        }),
        ('System Information', {
            'fields': ('id', 'uploaded_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_student_name(self, obj):
        """Display student name"""
        return obj.student.user.get_full_name()
    get_student_name.short_description = 'Student'


@admin.register(StudentNote)
class StudentNoteAdmin(admin.ModelAdmin):
    """Admin interface for Student Note model"""
    
    list_display = ('title', 'note_type', 'get_student_name', 'created_by', 'is_private', 'created_at')
    list_filter = ('note_type', 'is_private', 'created_at')
    search_fields = ('title', 'content', 'student__user__first_name', 'student__user__last_name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    
    fieldsets = (
        ('Student', {
            'fields': ('student',)
        }),
        ('Note Information', {
            'fields': ('note_type', 'title', 'content', 'is_private')
        }),
        ('Created By', {
            'fields': ('created_by',)
        }),
        ('System Information', {
            'fields': ('id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_student_name(self, obj):
        """Display student name"""
        return obj.student.user.get_full_name()
    get_student_name.short_description = 'Student'


@admin.register(StudentAchievement)
class StudentAchievementAdmin(admin.ModelAdmin):
    """Admin interface for Student Achievement model"""
    
    list_display = ('title', 'achievement_type', 'get_student_name', 'date_achieved', 'awarded_by')
    list_filter = ('achievement_type', 'date_achieved')
    search_fields = ('title', 'description', 'student__user__first_name', 'student__user__last_name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    date_hierarchy = 'date_achieved'
    
    fieldsets = (
        ('Student', {
            'fields': ('student',)
        }),
        ('Achievement Information', {
            'fields': ('achievement_type', 'title', 'description', 'date_achieved', 'awarded_by')
        }),
        ('Certificate', {
            'fields': ('certificate',)
        }),
        ('Recorded By', {
            'fields': ('recorded_by',)
        }),
        ('System Information', {
            'fields': ('id', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_student_name(self, obj):
        """Display student name"""
        return obj.student.user.get_full_name()
    get_student_name.short_description = 'Student'
