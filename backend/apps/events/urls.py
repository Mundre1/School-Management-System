from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, HolidayViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'holidays', HolidayViewSet, basename='holiday')

urlpatterns = [
    path('', include(router.urls)),
]
