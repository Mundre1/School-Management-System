from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassRoomViewSet, SubjectViewSet, PeriodViewSet, TimetableViewSet

router = DefaultRouter()
router.register(r'classrooms', ClassRoomViewSet, basename='classroom')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'periods', PeriodViewSet, basename='period')
router.register(r'timetables', TimetableViewSet, basename='timetable')

urlpatterns = [
    path('', include(router.urls)),
]
