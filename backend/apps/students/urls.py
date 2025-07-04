"""
Students App URLs
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet, GuardianViewSet, StudentDocumentViewSet,
    StudentNoteViewSet, StudentAchievementViewSet
)

app_name = 'students'

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'guardians', GuardianViewSet, basename='guardian')
router.register(r'documents', StudentDocumentViewSet, basename='student-document')
router.register(r'notes', StudentNoteViewSet, basename='student-note')
router.register(r'achievements', StudentAchievementViewSet, basename='student-achievement')

urlpatterns = [
    path('', include(router.urls)),
]
