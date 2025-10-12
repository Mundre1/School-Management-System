from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import ClassRoom, Subject, Period, Timetable
from .serializers import (
    ClassRoomSerializer, SubjectSerializer, PeriodSerializer,
    TimetableSerializer, TimetableDetailSerializer
)


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['grade', 'section', 'is_active']
    search_fields = ['name', 'room_number']
    ordering_fields = ['grade', 'section', 'created_at']
    ordering = ['grade', 'section']

    @action(detail=True, methods=['get'])
    def timetable(self, request, pk=None):
        """Get timetable for a specific classroom"""
        classroom = self.get_object()
        timetables = Timetable.objects.filter(classroom=classroom, is_active=True)
        serializer = TimetableDetailSerializer(timetables, many=True)
        return Response(serializer.data)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['grade', 'is_compulsory', 'is_active']
    search_fields = ['name', 'code']
    ordering_fields = ['grade', 'name', 'created_at']
    ordering = ['grade', 'name']


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['period_number']


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['classroom', 'day', 'subject', 'teacher', 'is_active']
    search_fields = ['classroom__name', 'subject__name', 'teacher__first_name', 'teacher__last_name']
    ordering_fields = ['day', 'period__period_number', 'created_at']
    ordering = ['day', 'period__period_number']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TimetableDetailSerializer
        return TimetableSerializer

    @action(detail=False, methods=['get'])
    def by_classroom(self, request):
        """Get timetable by classroom"""
        classroom_id = request.query_params.get('classroom_id')
        if not classroom_id:
            return Response({'error': 'classroom_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        timetables = self.queryset.filter(classroom_id=classroom_id, is_active=True)
        serializer = TimetableDetailSerializer(timetables, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_teacher(self, request):
        """Get timetable by teacher"""
        teacher_id = request.query_params.get('teacher_id')
        if not teacher_id:
            return Response({'error': 'teacher_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        timetables = self.queryset.filter(teacher_id=teacher_id, is_active=True)
        serializer = TimetableDetailSerializer(timetables, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_day(self, request):
        """Get timetable by day"""
        day = request.query_params.get('day')
        if not day:
            return Response({'error': 'day is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        timetables = self.queryset.filter(day=day, is_active=True)
        serializer = TimetableDetailSerializer(timetables, many=True)
        return Response(serializer.data)
