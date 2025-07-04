"""
Celery configuration for Smart School ERP System
Async task processing for emails, notifications, and scheduled tasks
"""

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('smart_school_erp')

# Load config from Django settings with CELERY namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from all installed apps
app.autodiscover_tasks()

# Celery Beat Schedule for periodic tasks
app.conf.beat_schedule = {
    # Send fee due reminders every day at 9 AM
    'send-fee-due-reminders': {
        'task': 'apps.fees.tasks.send_fee_due_reminders',
        'schedule': crontab(hour=9, minute=0),
    },
    # Send attendance notifications every day at 6 PM
    'send-attendance-notifications': {
        'task': 'apps.attendance.tasks.send_attendance_notifications',
        'schedule': crontab(hour=18, minute=0),
    },
    # Send assignment deadline reminders every day at 8 AM
    'send-assignment-reminders': {
        'task': 'apps.assignments.tasks.send_assignment_reminders',
        'schedule': crontab(hour=8, minute=0),
    },
    # Generate monthly attendance reports on 1st of every month
    'generate-monthly-attendance-reports': {
        'task': 'apps.attendance.tasks.generate_monthly_reports',
        'schedule': crontab(day_of_month=1, hour=0, minute=0),
    },
    # Send library book due reminders every day at 10 AM
    'send-library-due-reminders': {
        'task': 'apps.library.tasks.send_book_due_reminders',
        'schedule': crontab(hour=10, minute=0),
    },
    # Clean up expired OTPs every hour
    'cleanup-expired-otps': {
        'task': 'apps.authentication.tasks.cleanup_expired_otps',
        'schedule': crontab(minute=0),
    },
}

@app.task(bind=True)
def debug_task(self):
    """Debug task for testing Celery"""
    print(f'Request: {self.request!r}')
