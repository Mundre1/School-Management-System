from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .models import Event, Holiday
from .serializers import EventSerializer, HolidaySerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['event_type', 'target_classroom', 'is_public']
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['start_date', 'start_time', 'created_at']
    ordering = ['start_date', 'start_time']

    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        """Get upcoming events"""
        events = self.queryset.filter(start_date__gte=timezone.now().date())
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def ongoing(self, request):
        """Get ongoing events"""
        today = timezone.now().date()
        events = self.queryset.filter(start_date__lte=today, end_date__gte=today)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_month(self, request):
        """Get events by month"""
        year = request.query_params.get('year')
        month = request.query_params.get('month')
        
        if not year or not month:
            return Response({'error': 'year and month are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        events = self.queryset.filter(start_date__year=year, start_date__month=month)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Get events by type"""
        event_type = request.query_params.get('type')
        if not event_type:
            return Response({'error': 'type is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        events = self.queryset.filter(event_type=event_type)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)


class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_recurring']
    search_fields = ['name', 'description']
    ordering_fields = ['date', 'created_at']
    ordering = ['date']

    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        """Get upcoming holidays"""
        holidays = self.queryset.filter(date__gte=timezone.now().date())
        serializer = self.get_serializer(holidays, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_year(self, request):
        """Get holidays by year"""
        year = request.query_params.get('year')
        if not year:
            return Response({'error': 'year is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        holidays = self.queryset.filter(date__year=year)
        serializer = self.get_serializer(holidays, many=True)
        return Response(serializer.data)
