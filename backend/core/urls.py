"""
URL Configuration for Smart School ERP System
Professional API routing with versioning
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# Swagger temporarily disabled due to Python 3.13 compatibility
# Will be re-enabled once drf-yasg is updated


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    """API Root - Welcome endpoint"""
    return Response({
        'message': 'Welcome to Smart School ERP API',
        'version': '1.0.0',
        'endpoints': {
            'admin': '/admin/',
            'authentication': '/api/v1/auth/',
            'students': '/api/v1/students/',
            'staff': '/api/v1/staff/',
            'courses': '/api/v1/courses/',
            'attendance': '/api/v1/attendance/',
            'fees': '/api/v1/fees/',
            'results': '/api/v1/results/',
            'timetable': '/api/v1/timetable/',
            'assignments': '/api/v1/assignments/',
            'communication': '/api/v1/communication/',
            'library': '/api/v1/library/',
            'events': '/api/v1/events/',
            'leave': '/api/v1/leave/',
            'analytics': '/api/v1/analytics/',
        },
        'documentation': {
            'admin_panel': 'http://localhost:8000/admin/',
            'api_docs': 'Coming soon with Swagger/ReDoc'
        }
    })


urlpatterns = [
    # Root & API Root
    path('', api_root, name='api-root'),
    path('api/v1/', api_root, name='api-v1-root'),
    
    # Admin Panel
    path('admin/', admin.site.urls),
    
    # API Documentation - Temporarily disabled
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api-docs'),
    
    # API v1 Endpoints
    path('api/v1/auth/', include('apps.authentication.urls')),
    path('api/v1/students/', include('apps.students.urls')),
    path('api/v1/staff/', include('apps.staff.urls')),
    path('api/v1/courses/', include('apps.courses.urls')),
    path('api/v1/attendance/', include('apps.attendance.urls')),
    path('api/v1/fees/', include('apps.fees.urls')),
    path('api/v1/results/', include('apps.results.urls')),
    path('api/v1/timetable/', include('apps.timetable.urls')),
    path('api/v1/assignments/', include('apps.assignments.urls')),
    path('api/v1/communication/', include('apps.communication.urls')),
    path('api/v1/library/', include('apps.library.urls')),
    path('api/v1/events/', include('apps.events.urls')),
    path('api/v1/leave/', include('apps.leave.urls')),
    path('api/v1/analytics/', include('apps.analytics.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom Admin Site Configuration
admin.site.site_header = "Smart School ERP Administration"
admin.site.site_title = "Smart School ERP Admin"
admin.site.index_title = "Welcome to Smart School ERP System"
