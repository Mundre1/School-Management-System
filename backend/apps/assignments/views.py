from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .models import Assignment, AssignmentSubmission
from .serializers import AssignmentSerializer, AssignmentSubmissionSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['classroom', 'subject', 'teacher', 'status']
    search_fields = ['title', 'description']
    ordering_fields = ['due_date', 'created_at', 'total_marks']
    ordering = ['-created_at']

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        """Publish assignment"""
        assignment = self.get_object()
        assignment.status = 'published'
        assignment.save()
        return Response({'status': 'Assignment published'})

    @action(detail=True, methods=['post'])
    def close(self, request, pk=None):
        """Close assignment"""
        assignment = self.get_object()
        assignment.status = 'closed'
        assignment.save()
        return Response({'status': 'Assignment closed'})

    @action(detail=True, methods=['get'])
    def submissions(self, request, pk=None):
        """Get all submissions for an assignment"""
        assignment = self.get_object()
        submissions = assignment.submissions.all()
        serializer = AssignmentSubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def overdue(self, request):
        """Get overdue assignments"""
        assignments = self.queryset.filter(
            due_date__lt=timezone.now(),
            status='published'
        )
        serializer = self.get_serializer(assignments, many=True)
        return Response(serializer.data)


class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    queryset = AssignmentSubmission.objects.all()
    serializer_class = AssignmentSubmissionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['assignment', 'student', 'status']
    search_fields = ['student__first_name', 'student__last_name', 'assignment__title']
    ordering_fields = ['submitted_at', 'marks_obtained', 'created_at']
    ordering = ['-submitted_at']

    @action(detail=True, methods=['post'])
    def grade(self, request, pk=None):
        """Grade a submission"""
        submission = self.get_object()
        marks = request.data.get('marks_obtained')
        feedback = request.data.get('feedback', '')
        
        if marks is None:
            return Response({'error': 'marks_obtained is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        submission.marks_obtained = marks
        submission.feedback = feedback
        submission.status = 'graded'
        submission.graded_at = timezone.now()
        submission.graded_by = request.user.staff_profile if hasattr(request.user, 'staff_profile') else None
        submission.save()
        
        serializer = self.get_serializer(submission)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get pending submissions"""
        submissions = self.queryset.filter(status='pending')
        serializer = self.get_serializer(submissions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_student(self, request):
        """Get submissions by student"""
        student_id = request.query_params.get('student_id')
        if not student_id:
            return Response({'error': 'student_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        submissions = self.queryset.filter(student_id=student_id)
        serializer = self.get_serializer(submissions, many=True)
        return Response(serializer.data)
