from django.db import models
from apps.students.models import Student


class FeeStructure(models.Model):
    grade = models.IntegerField()
    academic_year = models.CharField(max_length=20)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    admission_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    exam_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    library_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sports_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['grade', 'academic_year']
        ordering = ['grade']

    def save(self, *args, **kwargs):
        self.total_fee = (
            self.tuition_fee + self.admission_fee + self.exam_fee +
            self.library_fee + self.sports_fee + self.other_fee
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Grade {self.grade} - {self.academic_year}"


class FeePayment(models.Model):
    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('partial', 'Partial'),
        ('overdue', 'Overdue'),
    ]
    
    PAYMENT_METHOD = [
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
        ('khalti', 'Khalti'),
        ('esewa', 'eSewa'),
        ('card', 'Card'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fee_payments')
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.SET_NULL, null=True)
    
    # Payment Details
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_remaining = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    due_date = models.DateField()
    
    # Transaction Details
    transaction_id = models.CharField(max_length=100, blank=True)
    receipt_number = models.CharField(max_length=50, unique=True, blank=True)
    remarks = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.amount_remaining = self.amount_due - self.amount_paid
        if self.amount_paid >= self.amount_due:
            self.payment_status = 'paid'
        elif self.amount_paid > 0:
            self.payment_status = 'partial'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.amount_due} - {self.payment_status}"
