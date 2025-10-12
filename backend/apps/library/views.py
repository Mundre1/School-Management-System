from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .models import Book, BookIssue
from .serializers import BookSerializer, BookIssueSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'is_active']
    search_fields = ['title', 'author', 'isbn', 'publisher']
    ordering_fields = ['title', 'author', 'publication_year', 'created_at']
    ordering = ['title']

    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get available books"""
        books = self.queryset.filter(available_copies__gt=0, is_active=True)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def issue_history(self, request, pk=None):
        """Get issue history for a book"""
        book = self.get_object()
        issues = book.issues.all()
        serializer = BookIssueSerializer(issues, many=True)
        return Response(serializer.data)


class BookIssueViewSet(viewsets.ModelViewSet):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['book', 'student', 'staff', 'status']
    search_fields = ['book__title', 'student__first_name', 'staff__first_name']
    ordering_fields = ['issue_date', 'due_date', 'return_date', 'created_at']
    ordering = ['-issue_date']

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        """Return a book"""
        issue = self.get_object()
        
        if issue.status == 'returned':
            return Response({'error': 'Book already returned'}, status=status.HTTP_400_BAD_REQUEST)
        
        issue.return_date = timezone.now().date()
        issue.status = 'returned'
        
        # Calculate fine if overdue
        if issue.is_overdue:
            fine_per_day = request.data.get('fine_per_day', 10)
            issue.calculate_fine(fine_per_day)
        
        issue.save()
        
        # Increase available copies
        book = issue.book
        book.available_copies += 1
        book.save()
        
        serializer = self.get_serializer(issue)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def overdue(self, request):
        """Get overdue books"""
        issues = self.queryset.filter(
            status='issued',
            due_date__lt=timezone.now().date()
        )
        # Update status to overdue
        for issue in issues:
            issue.status = 'overdue'
            issue.calculate_fine()
        
        serializer = self.get_serializer(issues, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_student(self, request):
        """Get books issued to a student"""
        student_id = request.query_params.get('student_id')
        if not student_id:
            return Response({'error': 'student_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        issues = self.queryset.filter(student_id=student_id)
        serializer = self.get_serializer(issues, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get library statistics"""
        total_books = Book.objects.count()
        available_books = Book.objects.filter(available_copies__gt=0).count()
        issued_books = self.queryset.filter(status='issued').count()
        overdue_books = self.queryset.filter(status='overdue').count()
        
        return Response({
            'total_books': total_books,
            'available_books': available_books,
            'issued_books': issued_books,
            'overdue_books': overdue_books,
        })
