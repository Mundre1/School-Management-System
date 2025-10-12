from django.urls import path
from .views import (
    DashboardAnalyticsView,
    StudentAnalyticsView,
    AttendanceAnalyticsView,
    FeeAnalyticsView,
    ResultAnalyticsView
)

urlpatterns = [
    path('dashboard/', DashboardAnalyticsView.as_view(), name='dashboard-analytics'),
    path('students/', StudentAnalyticsView.as_view(), name='student-analytics'),
    path('attendance/', AttendanceAnalyticsView.as_view(), name='attendance-analytics'),
    path('fees/', FeeAnalyticsView.as_view(), name='fee-analytics'),
    path('results/', ResultAnalyticsView.as_view(), name='result-analytics'),
]
