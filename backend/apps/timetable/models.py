from django.db import models
from apps.students.models import Student
from apps.staff.models import Staff


class ClassRoom(models.Model):
    """Classroom/Section model"""
    name = models.CharField(max_length=100)  # e.g., "Grade 10 - A"
    grade = models.IntegerField()
    section = models.CharField(max_length=10)
    capacity = models.IntegerField(default=40)
    room_number = models.CharField(max_length=20, blank=True)
    class_teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, related_name='class_teacher_of')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'classrooms'
        ordering = ['grade', 'section']
        unique_together = ['grade', 'section']

    def __str__(self):
        return f"Grade {self.grade} - {self.section}"


class Subject(models.Model):
    """Subject model"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    grade = models.IntegerField()
    is_compulsory = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'subjects'
        ordering = ['grade', 'name']

    def __str__(self):
        return f"{self.name} ({self.code})"


class Period(models.Model):
    """Period/Time slot model"""
    PERIOD_CHOICES = [
        (1, 'Period 1'),
        (2, 'Period 2'),
        (3, 'Period 3'),
        (4, 'Period 4'),
        (5, 'Period 5'),
        (6, 'Period 6'),
        (7, 'Period 7'),
        (8, 'Period 8'),
    ]
    
    period_number = models.IntegerField(choices=PERIOD_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_break = models.BooleanField(default=False)
    break_name = models.CharField(max_length=50, blank=True)  # e.g., "Lunch Break"
    
    class Meta:
        db_table = 'periods'
        ordering = ['period_number']
        unique_together = ['period_number', 'start_time']

    def __str__(self):
        if self.is_break:
            return f"{self.break_name} ({self.start_time} - {self.end_time})"
        return f"Period {self.period_number} ({self.start_time} - {self.end_time})"


class Timetable(models.Model):
    """Timetable model"""
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name='timetables')
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='teaching_slots')
    room_number = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'timetables'
        ordering = ['day', 'period__period_number']
        unique_together = ['classroom', 'day', 'period']

    def __str__(self):
        return f"{self.classroom} - {self.day} - {self.period}"
