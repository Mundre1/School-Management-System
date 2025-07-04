"""
Student Views
API views for student management
"""

from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from apps.authentication.permissions import IsAdmin, IsAdminOrStaff
from .models import Student, Guardian, StudentDocument, StudentNote, StudentAchievement
from .serializers import (
    StudentSerializer, StudentDetailSerializer, StudentListSerializer,
    StudentCreateSerializer, GuardianSerializer, StudentDocumentSerializer,
    StudentNoteSerializer, StudentAchievementSerializer
)


class StudentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Student CRUD operations
    Admin and Staff can manage students
    Students can view their own profile
    """
    
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'class_name', 'section', 'academic_year', 'admission_type']
    search_fields = ['admission_number', 'roll_number', 'user__first_name', 'user__last_name', 'user__email']
    ordering_fields = ['admission_number', 'admission_date', 'created_at']
    ordering = ['admission_number']
    
    def get_queryset(self):
        """Filter queryset based on user role"""
        user = self.request.user
        
        if user.is_admin or user.is_teacher:
            # Admin and staff can see all students
            return Student.objects.select_related('user').prefetch_related('guardians')
        elif user.is_student_user:
            # Students can only see their own profile
            return Student.objects.filter(user=user).select_related('user').prefetch_related('guardians')
        
        return Student.objects.none()
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action == 'list':
            return StudentListSerializer
        elif self.action == 'retrieve':
            return StudentDetailSerializer
        elif self.action == 'create':
            return StudentCreateSerializer
        return StudentSerializer
    
    def get_permissions(self):
        """Set permissions based on action"""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminOrStaff()]
        return [IsAuthenticated()]
    
    @action(detail=False, methods=['get'])
    def my_profile(self, request):
        """Get current student's profile"""
        if not request.user.is_student_user:
            return Response(
                {'error': 'Only students can access this endpoint'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        try:
            student = Student.objects.get(user=request.user)
            serializer = StudentDetailSerializer(student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response(
                {'error': 'Student profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['get'])
    def by_class(self, request):
        """Get students by class and section"""
        class_name = request.query_params.get('class_name')
        section = request.query_params.get('section')
        
        if not class_name:
            return Response(
                {'error': 'class_name parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        queryset = self.get_queryset().filter(class_name=class_name)
        if section:
            queryset = queryset.filter(section=section)
        
        serializer = StudentListSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def guardians(self, request, pk=None):
        """Get all guardians for a student"""
        student = self.get_object()
        guardians = student.guardians.all()
        serializer = GuardianSerializer(guardians, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def documents(self, request, pk=None):
        """Get all documents for a student"""
        student = self.get_object()
        documents = student.documents.all()
        serializer = StudentDocumentSerializer(documents, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def achievements(self, request, pk=None):
        """Get all achievements for a student"""
        student = self.get_object()
        achievements = student.achievements.all()
        serializer = StudentAchievementSerializer(achievements, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        """Change student status"""
        student = self.get_object()
        new_status = request.data.get('status')
        
        if new_status not in dict(Student.STATUS_CHOICES):
            return Response(
                {'error': 'Invalid status'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        student.status = new_status
        student.save()
        
        serializer = StudentSerializer(student)
        return Response(serializer.data)


class GuardianViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Guardian CRUD operations
    Admin and Staff can manage guardians
    """
    
    queryset = Guardian.objects.select_related('student', 'student__user')
    serializer_class = GuardianSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaff]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['student', 'relation', 'is_primary', 'is_emergency_contact']
    search_fields = ['name', 'phone', 'email']
    
    @action(detail=False, methods=['get'])
    def by_student(self, request):
        """Get guardians by student ID"""
        student_id = request.query_params.get('student_id')
        
        if not student_id:
            return Response(
                {'error': 'student_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        guardians = self.queryset.filter(student_id=student_id)
        serializer = self.serializer_class(guardians, many=True)
        return Response(serializer.data)


class StudentDocumentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Student Document CRUD operations
    Admin and Staff can manage documents
    """
    
    queryset = StudentDocument.objects.select_related('student', 'student__user', 'uploaded_by')
    serializer_class = StudentDocumentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaff]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['student', 'document_type']
    search_fields = ['document_name', 'description']
    
    def perform_create(self, serializer):
        """Set uploaded_by to current user"""
        serializer.save(uploaded_by=self.request.user)
    
    @action(detail=False, methods=['get'])
    def by_student(self, request):
        """Get documents by student ID"""
        student_id = request.query_params.get('student_id')
        
        if not student_id:
            return Response(
                {'error': 'student_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        documents = self.queryset.filter(student_id=student_id)
        serializer = self.serializer_class(documents, many=True)
        return Response(serializer.data)


class StudentNoteViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Student Note CRUD operations
    Admin and Staff can manage notes
    """
    
    queryset = StudentNote.objects.select_related('student', 'student__user', 'created_by')
    serializer_class = StudentNoteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaff]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['student', 'note_type', 'is_private']
    search_fields = ['title', 'content']
    
    def get_queryset(self):
        """Filter private notes for non-admin users"""
        queryset = super().get_queryset()
        
        if not self.request.user.is_admin:
            # Non-admin staff can't see private notes
            queryset = queryset.filter(is_private=False)
        
        return queryset
    
    def perform_create(self, serializer):
        """Set created_by to current user"""
        serializer.save(created_by=self.request.user)
    
    @action(detail=False, methods=['get'])
    def by_student(self, request):
        """Get notes by student ID"""
        student_id = request.query_params.get('student_id')
        
        if not student_id:
            return Response(
                {'error': 'student_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        notes = self.get_queryset().filter(student_id=student_id)
        serializer = self.serializer_class(notes, many=True)
        return Response(serializer.data)


class StudentAchievementViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Student Achievement CRUD operations
    Admin and Staff can manage achievements
    """
    
    queryset = StudentAchievement.objects.select_related('student', 'student__user', 'recorded_by')
    serializer_class = StudentAchievementSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaff]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['student', 'achievement_type']
    search_fields = ['title', 'description', 'awarded_by']
    ordering_fields = ['date_achieved', 'created_at']
    ordering = ['-date_achieved']
    
    def perform_create(self, serializer):
        """Set recorded_by to current user"""
        serializer.save(recorded_by=self.request.user)
    
    @action(detail=False, methods=['get'])
    def by_student(self, request):
        """Get achievements by student ID"""
        student_id = request.query_params.get('student_id')
        
        if not student_id:
            return Response(
                {'error': 'student_id parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        achievements = self.queryset.filter(student_id=student_id)
        serializer = self.serializer_class(achievements, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Get achievements by type"""
        achievement_type = request.query_params.get('type')
        
        if not achievement_type:
            return Response(
                {'error': 'type parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        achievements = self.queryset.filter(achievement_type=achievement_type)
        serializer = self.serializer_class(achievements, many=True)
        return Response(serializer.data)
