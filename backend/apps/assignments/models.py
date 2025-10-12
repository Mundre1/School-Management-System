from django.db import models
from apps.students.models import Student
from apps.staff.models import Staff
from apps.timetable.models import ClassRoom, Subject


class Assignment(models.Model):
    """Assignment model"""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('closed', 'Closed'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name='assignments')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='assignments')
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='created_assignments')
    total_marks = models.IntegerField(default=100)
    due_date = models.DateTimeField()
    attachment = models.FileField(upload_to='assignments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'assignments'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.classroom}"

    @property
    def is_overdue(self):
        from django.utils import timezone
        return timezone.now() > self.due_date and self.status == 'published'

    @property
    def submission_count(self):
        return self.submissions.count()

    @property
    def pending_count(self):
        total_students = self.classroom.students.count() if hasattr(self.classroom, 'students') else 0
        return total_students - self.submission_count


class AssignmentSubmission(models.Model):
    """Assignment submission model"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('submitted', 'Submitted'),
        ('graded', 'Graded'),
        ('late', 'Late Submission'),
    ]
    
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    submission_text = models.TextField(blank=True)
    attachment = models.FileField(upload_to='submissions/', blank=True, null=True)
    marks_obtained = models.IntegerField(null=True, blank=True)
    feedback = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(null=True, blank=True)
    graded_at = models.DateTimeField(null=True, blank=True)
    graded_by = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='graded_submissions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'assignment_submissions'
        ordering = ['-submitted_at']
        unique_together = ['assignment', 'student']

    def __str__(self):
        return f"{self.assignment.title} - {self.student.get_full_name()}"

    @property
    def is_late(self):
        if self.submitted_at:
            return self.submitted_at > self.assignment.due_date
        return False

    @property
    def percentage(self):
        if self.marks_obtained is not None and self.assignment.total_marks > 0:
            return round((self.marks_obtained / self.assignment.total_marks) * 100, 2)
        return None
