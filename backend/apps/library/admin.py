from django.contrib import admin
from .models import Book, BookIssue


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'category', 'total_copies', 'available_copies', 'is_active']
    list_filter = ['category', 'is_active', 'publication_year']
    search_fields = ['title', 'author', 'isbn', 'publisher']
    ordering = ['title']


@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):
    list_display = ['book', 'get_borrower', 'issue_date', 'due_date', 'return_date', 'status', 'fine_amount']
    list_filter = ['status', 'issue_date', 'due_date']
    search_fields = ['book__title', 'student__first_name', 'staff__first_name']
    ordering = ['-issue_date']

    def get_borrower(self, obj):
        return obj.student or obj.staff
    get_borrower.short_description = 'Borrower'
