from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg, Count, Q
from .models import Exam, Subject, Result
from .serializers import ExamSerializer, SubjectSerializer, ResultSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['grade', 'exam_type', 'academic_year']
    search_fields = ['name']
    ordering_fields = ['start_date', 'created_at']
    ordering = ['-start_date']


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['grade']
    search_fields = ['name', 'code']
    ordering_fields = ['grade', 'name']
    ordering = ['grade', 'name']


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['student', 'exam', 'subject', 'grade']
    search_fields = ['student__first_name', 'student__last_name']
    ordering_fields = ['created_at', 'percentage']
    ordering = ['-created_at']

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get result statistics"""
        exam_id = request.query_params.get('exam')
        grade = request.query_params.get('grade')
        
        queryset = self.queryset
        if exam_id:
            queryset = queryset.filter(exam_id=exam_id)
        if grade:
            queryset = queryset.filter(student__grade=grade)
        
        stats = queryset.aggregate(
            total_results=Count('id'),
            average_percentage=Avg('percentage'),
            pass_count=Count('id', filter=Q(percentage__gte=40)),
            fail_count=Count('id', filter=Q(percentage__lt=40)),
            a_plus_count=Count('id', filter=Q(grade='A+')),
            a_count=Count('id', filter=Q(grade='A')),
            b_count=Count('id', filter=Q(grade__startswith='B')),
            c_count=Count('id', filter=Q(grade__startswith='C')),
        )
        
        if stats['total_results'] > 0:
            stats['pass_percentage'] = round((stats['pass_count'] / stats['total_results']) * 100, 2)
        else:
            stats['pass_percentage'] = 0
        
        return Response(stats)

    @action(detail=False, methods=['get'])
    def student_report(self, request):
        """Get complete report for a student"""
        student_id = request.query_params.get('student_id')
        exam_id = request.query_params.get('exam_id')
        
        if not student_id:
            return Response({'error': 'student_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.queryset.filter(student_id=student_id)
        if exam_id:
            queryset = queryset.filter(exam_id=exam_id)
        
        results = self.get_serializer(queryset, many=True).data
        
        # Calculate overall statistics
        if results:
            total_marks = sum(r['marks_obtained'] for r in results)
            max_marks = sum(r['total_marks'] for r in results)
            overall_percentage = (total_marks / max_marks * 100) if max_marks > 0 else 0
            
            report = {
                'results': results,
                'total_subjects': len(results),
                'total_marks_obtained': total_marks,
                'total_marks': max_marks,
                'overall_percentage': round(overall_percentage, 2),
                'pass_count': sum(1 for r in results if r['percentage'] >= 40),
                'fail_count': sum(1 for r in results if r['percentage'] < 40),
            }
        else:
            report = {
                'results': [],
                'message': 'No results found'
            }
        
        return Response(report)

    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        """Create multiple results at once"""
        results_data = request.data.get('results', [])
        
        if not results_data:
            return Response({'error': 'results data is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        created_results = []
        errors = []
        
        for result_data in results_data:
            serializer = self.get_serializer(data=result_data)
            if serializer.is_valid():
                serializer.save()
                created_results.append(serializer.data)
            else:
                errors.append({
                    'data': result_data,
                    'errors': serializer.errors
                })
        
        return Response({
            'created': len(created_results),
            'failed': len(errors),
            'results': created_results,
            'errors': errors
        }, status=status.HTTP_201_CREATED if created_results else status.HTTP_400_BAD_REQUEST)
