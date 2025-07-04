from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExamViewSet, SubjectViewSet, ResultViewSet

app_name = 'results'

router = DefaultRouter()
router.register(r'exams', ExamViewSet, basename='exam')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'results', ResultViewSet, basename='result')

urlpatterns = [
    path('', include(router.urls)),
]
