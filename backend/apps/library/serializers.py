from rest_framework import serializers
from .models import Book, BookIssue


class BookSerializer(serializers.ModelSerializer):
    is_available = serializers.BooleanField(read_only=True)
    issued_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_issued_count(self, obj):
        return obj.issues.filter(status='issued').count()


class BookIssueSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    book_author = serializers.CharField(source='book.author', read_only=True)
    borrower_name = serializers.SerializerMethodField()
    issued_by_name = serializers.CharField(source='issued_by.get_full_name', read_only=True)
    is_overdue = serializers.BooleanField(read_only=True)
    days_overdue = serializers.IntegerField(read_only=True)

    class Meta:
        model = BookIssue
        fields = '__all__'

    def get_borrower_name(self, obj):
        if obj.student:
            return obj.student.get_full_name()
        elif obj.staff:
            return obj.staff.get_full_name()
        return None

    def create(self, validated_data):
        book = validated_data['book']
        if book.available_copies <= 0:
            raise serializers.ValidationError("Book is not available")
        
        # Decrease available copies
        book.available_copies -= 1
        book.save()
        
        return super().create(validated_data)
