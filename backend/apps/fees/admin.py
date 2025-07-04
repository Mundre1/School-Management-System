from django.contrib import admin
from .models import FeeStructure, FeePayment


@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ['grade', 'academic_year', 'total_fee', 'created_at']
    list_filter = ['grade', 'academic_year']
    ordering = ['grade']


@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ['student', 'amount_due', 'amount_paid', 'payment_status', 'due_date', 'payment_date']
    list_filter = ['payment_status', 'payment_method', 'payment_date']
    search_fields = ['student__first_name', 'student__last_name', 'receipt_number']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
