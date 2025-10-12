from django.db import models
from apps.students.models import Student
from apps.staff.models import Staff
from datetime import timedelta
from django.utils import timezone


class Book(models.Model):
    """Book model"""
    CATEGORY_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('mathematics', 'Mathematics'),
        ('history', 'History'),
        ('geography', 'Geography'),
        ('literature', 'Literature'),
        ('reference', 'Reference'),
        ('magazine', 'Magazine'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    publisher = models.CharField(max_length=200, blank=True)
    publication_year = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)
    rack_number = models.CharField(max_length=20, blank=True)
    cover_image = models.ImageField(upload_to='books/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'books'
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author}"

    @property
    def is_available(self):
        return self.available_copies > 0


class BookIssue(models.Model):
    """Book issue/borrow model"""
    STATUS_CHOICES = [
        ('issued', 'Issued'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
        ('lost', 'Lost'),
    ]
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='issues')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True, related_name='book_issues')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True, related_name='book_issues')
    issued_by = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, related_name='issued_books')
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='issued')
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book_issues'
        ordering = ['-issue_date']

    def __str__(self):
        borrower = self.student or self.staff
        return f"{self.book.title} - {borrower}"

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = timezone.now().date() + timedelta(days=14)
        super().save(*args, **kwargs)

    @property
    def is_overdue(self):
        if self.status == 'issued' and self.due_date:
            return timezone.now().date() > self.due_date
        return False

    @property
    def days_overdue(self):
        if self.is_overdue:
            return (timezone.now().date() - self.due_date).days
        return 0

    def calculate_fine(self, fine_per_day=10):
        """Calculate fine for overdue books"""
        if self.is_overdue:
            self.fine_amount = self.days_overdue * fine_per_day
            self.status = 'overdue'
            self.save()
        return self.fine_amount
