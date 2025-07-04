from django.db import models
from apps.students.models import Student


class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('midterm', 'Mid Term'),
        ('final', 'Final'),
        ('unit_test', 'Unit Test'),
        ('practical', 'Practical'),
    ]

    name = models.CharField(max_length=200)
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES)
    grade = models.IntegerField()
    academic_year = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    total_marks = models.IntegerField(default=100)
    passing_marks = models.IntegerField(default=40)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.name} - Grade {self.grade}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    grade = models.IntegerField()
    description = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['grade', 'name']

    def __str__(self):
        return f"{self.name} ({self.code}) - Grade {self.grade}"


class Result(models.Model):
    GRADE_CHOICES = [
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='results')
    
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.IntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    grade = models.CharField(max_length=5, choices=GRADE_CHOICES, blank=True)
    remarks = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['student', 'exam', 'subject']
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Calculate percentage
        self.percentage = (self.marks_obtained / self.total_marks) * 100
        
        # Assign grade based on percentage
        if self.percentage >= 90:
            self.grade = 'A+'
        elif self.percentage >= 80:
            self.grade = 'A'
        elif self.percentage >= 70:
            self.grade = 'B+'
        elif self.percentage >= 60:
            self.grade = 'B'
        elif self.percentage >= 50:
            self.grade = 'C+'
        elif self.percentage >= 40:
            self.grade = 'C'
        elif self.percentage >= 30:
            self.grade = 'D'
        else:
            self.grade = 'F'
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.subject}: {self.marks_obtained}/{self.total_marks}"
