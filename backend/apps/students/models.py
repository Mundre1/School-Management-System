"""
Student Models
Complete student management with profiles, guardians, and academic records
Reflecting professional Django development from Code IT internship
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from apps.authentication.models import User
import uuid


class Student(models.Model):
    """
    Student Profile Model
    Extended profile for students with academic information
    """
    
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('GRADUATED', 'Graduated'),
        ('SUSPENDED', 'Suspended'),
        ('TRANSFERRED', 'Transferred'),
    )
    
    ADMISSION_TYPE_CHOICES = (
        ('REGULAR', 'Regular'),
        ('TRANSFER', 'Transfer'),
        ('SCHOLARSHIP', 'Scholarship'),
    )
    
    # Primary Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    
    # Academic Information
    admission_number = models.CharField(max_length=50, unique=True, db_index=True)
    roll_number = models.CharField(max_length=50, blank=True, null=True)
    class_name = models.CharField(max_length=50)  # e.g., "Grade 10", "Class 12"
    section = models.CharField(max_length=10, blank=True, null=True)  # e.g., "A", "B"
    academic_year = models.CharField(max_length=20)  # e.g., "2025-2026"
    
    # Admission Details
    admission_date = models.DateField()
    admission_type = models.CharField(max_length=20, choices=ADMISSION_TYPE_CHOICES, default='REGULAR')
    previous_school = models.CharField(max_length=255, blank=True, null=True)
    
    # Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    
    # Guardian Information (Primary)
    father_name = models.CharField(max_length=200)
    father_phone = models.CharField(max_length=17, blank=True, null=True)
    father_email = models.EmailField(blank=True, null=True)
    father_occupation = models.CharField(max_length=100, blank=True, null=True)
    
    mother_name = models.CharField(max_length=200)
    mother_phone = models.CharField(max_length=17, blank=True, null=True)
    mother_email = models.EmailField(blank=True, null=True)
    mother_occupation = models.CharField(max_length=100, blank=True, null=True)
    
    # Medical Information
    medical_conditions = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    
    # Documents
    birth_certificate = models.FileField(upload_to='students/documents/', blank=True, null=True)
    transfer_certificate = models.FileField(upload_to='students/documents/', blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['admission_number']
        indexes = [
            models.Index(fields=['admission_number']),
            models.Index(fields=['class_name', 'section']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"{self.admission_number} - {self.user.get_full_name()}"
    
    @property
    def full_class(self):
        """Return full class name with section"""
        if self.section:
            return f"{self.class_name} - {self.section}"
        return self.class_name
    
    @property
    def age(self):
        """Calculate student age"""
        if self.user.date_of_birth:
            today = timezone.now().date()
            return today.year - self.user.date_of_birth.year - (
                (today.month, today.day) < (self.user.date_of_birth.month, self.user.date_of_birth.day)
            )
        return None


class Guardian(models.Model):
    """
    Guardian Model
    Additional guardians beyond parents
    """
    
    RELATION_CHOICES = (
        ('FATHER', 'Father'),
        ('MOTHER', 'Mother'),
        ('GRANDFATHER', 'Grandfather'),
        ('GRANDMOTHER', 'Grandmother'),
        ('UNCLE', 'Uncle'),
        ('AUNT', 'Aunt'),
        ('SIBLING', 'Sibling'),
        ('OTHER', 'Other'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='guardians')
    
    # Guardian Information
    name = models.CharField(max_length=200)
    relation = models.CharField(max_length=20, choices=RELATION_CHOICES)
    phone = models.CharField(max_length=17)
    email = models.EmailField(blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    # Priority
    is_primary = models.BooleanField(default=False)
    is_emergency_contact = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'guardians'
        verbose_name = 'Guardian'
        verbose_name_plural = 'Guardians'
        ordering = ['-is_primary', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.relation}) - {self.student.user.get_full_name()}"


class StudentDocument(models.Model):
    """
    Student Documents Model
    Store various student documents
    """
    
    DOCUMENT_TYPE_CHOICES = (
        ('ID_CARD', 'ID Card'),
        ('BIRTH_CERTIFICATE', 'Birth Certificate'),
        ('TRANSFER_CERTIFICATE', 'Transfer Certificate'),
        ('MARKSHEET', 'Marksheet'),
        ('MEDICAL', 'Medical Certificate'),
        ('CHARACTER', 'Character Certificate'),
        ('PHOTO', 'Photograph'),
        ('OTHER', 'Other'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='documents')
    
    document_type = models.CharField(max_length=30, choices=DOCUMENT_TYPE_CHOICES)
    document_name = models.CharField(max_length=255)
    document_file = models.FileField(upload_to='students/documents/')
    description = models.TextField(blank=True, null=True)
    
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='uploaded_student_documents')
    
    # Timestamps
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'student_documents'
        verbose_name = 'Student Document'
        verbose_name_plural = 'Student Documents'
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.document_name} - {self.student.user.get_full_name()}"


class StudentNote(models.Model):
    """
    Student Notes Model
    Internal notes about students for staff reference
    """
    
    NOTE_TYPE_CHOICES = (
        ('ACADEMIC', 'Academic'),
        ('BEHAVIORAL', 'Behavioral'),
        ('MEDICAL', 'Medical'),
        ('GENERAL', 'General'),
        ('ACHIEVEMENT', 'Achievement'),
        ('CONCERN', 'Concern'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='notes')
    
    note_type = models.CharField(max_length=20, choices=NOTE_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='student_notes')
    is_private = models.BooleanField(default=False)  # Only visible to admin
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'student_notes'
        verbose_name = 'Student Note'
        verbose_name_plural = 'Student Notes'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.student.user.get_full_name()}"


class StudentAchievement(models.Model):
    """
    Student Achievements Model
    Track student achievements and awards
    """
    
    ACHIEVEMENT_TYPE_CHOICES = (
        ('ACADEMIC', 'Academic Excellence'),
        ('SPORTS', 'Sports'),
        ('CULTURAL', 'Cultural'),
        ('LEADERSHIP', 'Leadership'),
        ('COMPETITION', 'Competition'),
        ('SERVICE', 'Community Service'),
        ('OTHER', 'Other'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='achievements')
    
    achievement_type = models.CharField(max_length=20, choices=ACHIEVEMENT_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_achieved = models.DateField()
    
    certificate = models.FileField(upload_to='students/achievements/', blank=True, null=True)
    
    awarded_by = models.CharField(max_length=255, blank=True, null=True)
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='recorded_achievements')
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'student_achievements'
        verbose_name = 'Student Achievement'
        verbose_name_plural = 'Student Achievements'
        ordering = ['-date_achieved']
    
    def __str__(self):
        return f"{self.title} - {self.student.user.get_full_name()}"
