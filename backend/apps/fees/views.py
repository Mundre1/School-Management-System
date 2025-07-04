from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Count, Q
from .models import FeeStructure, FeePayment
from .serializers import FeeStructureSerializer, FeePaymentSerializer


class FeeStructureViewSet(viewsets.ModelViewSet):
    queryset = FeeStructure.objects.all()
    serializer_class = FeeStructureSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['grade', 'academic_year']
    ordering_fields = ['grade', 'total_fee']
    ordering = ['grade']


class FeePaymentViewSet(viewsets.ModelViewSet):
    queryset = FeePayment.objects.all()
    serializer_class = FeePaymentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['student', 'payment_status', 'payment_method']
    search_fields = ['student__first_name', 'student__last_name', 'receipt_number', 'transaction_id']
    ordering_fields = ['created_at', 'due_date', 'amount_due']
    ordering = ['-created_at']

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """Get fee payment statistics"""
        stats = self.queryset.aggregate(
            total_due=Sum('amount_due'),
            total_paid=Sum('amount_paid'),
            total_remaining=Sum('amount_remaining'),
            total_payments=Count('id'),
            paid_count=Count('id', filter=Q(payment_status='paid')),
            pending_count=Count('id', filter=Q(payment_status='pending')),
            partial_count=Count('id', filter=Q(payment_status='partial')),
            overdue_count=Count('id', filter=Q(payment_status='overdue'))
        )
        
        if stats['total_due']:
            stats['collection_percentage'] = round((stats['total_paid'] / stats['total_due']) * 100, 2)
        else:
            stats['collection_percentage'] = 0
        
        return Response(stats)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get all pending payments"""
        pending = self.queryset.filter(payment_status__in=['pending', 'partial', 'overdue'])
        serializer = self.get_serializer(pending, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def make_payment(self, request, pk=None):
        """Make a payment for a fee"""
        fee_payment = self.get_object()
        amount = request.data.get('amount')
        payment_method = request.data.get('payment_method')
        transaction_id = request.data.get('transaction_id', '')
        
        if not amount:
            return Response({'error': 'Amount is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            amount = float(amount)
            fee_payment.amount_paid += amount
            fee_payment.payment_method = payment_method
            fee_payment.transaction_id = transaction_id
            
            if not fee_payment.payment_date:
                from datetime import date
                fee_payment.payment_date = date.today()
            
            fee_payment.save()
            
            serializer = self.get_serializer(fee_payment)
            return Response(serializer.data)
        except ValueError:
            return Response({'error': 'Invalid amount'}, status=status.HTTP_400_BAD_REQUEST)
