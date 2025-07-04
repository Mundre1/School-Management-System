# Core Django Application
from __future__ import absolute_import, unicode_literals

# Celery is optional for development
try:
    from .celery import app as celery_app
    __all__ = ('celery_app',)
except ImportError:
    # Celery not installed - skip for development
    pass
