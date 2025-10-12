from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .models import LeaveApplication
from .serializers import LeaveApplicationSerializer


class LeaveApplicationViewSet(viewsets.ModelViewSet):
    queryset = LeaveApplication.objects.all()
    serializer_class = LeaveApplicationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['student', 'staff', 'leave_type', 'status']
    search_fields = ['reason', 'student__first_name', 'staff__first_name']
    ordering_fields = ['start_date', 'created_at', 'status']
    ordering = ['-created_at']

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Approve leave application"""
        leave = self.get_object()
        
        if leave.status != 'pending':
            return Response({'error': 'Leave is not pending'}, status=status.HTTP_400_BAD_REQUEST)
        
        leave.status = 'approved'
        leave.approved_at = timezone.now()
        leave.approved_by = request.user.staff_profile if hasattr(request.user, 'staff_profile') else None
        leave.approval_remarks = request.data.get('remarks', '')
        leave.save()
        
        serializer = self.get_serializer(leave)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        """Reject leave application"""
        leave = self.get_object()
        
        if leave.status != 'pending':
            return Response({'error': 'Leave is not pending'}, status=status.HTTP_400_BAD_REQUEST)
        
        leave.status = 'rejected'
        leave.approved_at = timezone.now()
        leave.approved_by = request.user.staff_profile if hasattr(request.user, 'staff_profile') else None
        leave.approval_remarks = request.data.get('remarks', '')
        leave.save()
        
        serializer = self.get_serializer(leave)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get pending leave applications"""
        leaves = self.queryset.filter(status='pending')
        serializer = self.get_serializer(leaves, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_student(self, request):
        """Get leave applications by student"""
        student_id = request.query_params.get('student_id')
        if not student_id:
            return Response({'error': 'student_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        leaves = self.queryset.filter(student_id=student_id)
        serializer = self.get_serializer(leaves, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_staff(self, request):
        """Get leave applications by staff"""
        staff_id = request.query_params.get('staff_id')
        if not staff_id:
            return Response({'error': 'staff_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        leaves = self.queryset.filter(staff_id=staff_id)
        serializer = self.get_serializer(leaves, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get leave statistics"""
        total = self.queryset.count()
        pending = self.queryset.filter(status='pending').count()
        approved = self.queryset.filter(status='approved').count()
        rejected = self.queryset.filter(status='rejected').count()
        
        return Response({
            'total': total,
            'pending': pending,
            'approved': approved,
            'rejected': rejected,
        })
