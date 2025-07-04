from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count, Q
from datetime import datetime, timedelta
from .models import Attendance
from .serializers import AttendanceSerializer, BulkAttendanceSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['student', 'date', 'status']
    search_fields = ['student__first_name', 'student__last_name']
    ordering_fields = ['date', 'marked_at']
    ordering = ['-date']

    @action(detail=False, methods=['post'])
    def bulk_mark(self, request):
        """Mark attendance for multiple students at once"""
        serializer = BulkAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            date = serializer.validated_data['date']
            attendances_data = serializer.validated_data['attendances']
            
            created_attendances = []
            for att_data in attendances_data:
                attendance, created = Attendance.objects.update_or_create(
                    student_id=att_data['student_id'],
                    date=date,
                    defaults={
                        'status': att_data['status'],
                        'remarks': att_data.get('remarks', ''),
                        'marked_by': request.user.email
                    }
                )
                created_attendances.append(attendance)
            
            return Response({
                'message': f'Attendance marked for {len(created_attendances)} students',
                'count': len(created_attendances)
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get attendance statistics"""
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        
        queryset = self.queryset
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)
        
        stats = queryset.aggregate(
            total=Count('id'),
            present=Count('id', filter=Q(status='present')),
            absent=Count('id', filter=Q(status='absent')),
            late=Count('id', filter=Q(status='late')),
            excused=Count('id', filter=Q(status='excused'))
        )
        
        if stats['total'] > 0:
            stats['present_percentage'] = round((stats['present'] / stats['total']) * 100, 2)
            stats['absent_percentage'] = round((stats['absent'] / stats['total']) * 100, 2)
        else:
            stats['present_percentage'] = 0
            stats['absent_percentage'] = 0
        
        return Response(stats)

    @action(detail=False, methods=['get'])
    def by_date(self, request):
        """Get attendance for a specific date"""
        date = request.query_params.get('date', datetime.now().date())
        grade = request.query_params.get('grade')
        
        queryset = self.queryset.filter(date=date)
        if grade:
            queryset = queryset.filter(student__grade=grade)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
