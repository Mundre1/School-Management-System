#!/usr/bin/env python
"""
Script to create superuser automatically
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.authentication.models import User

# Create superuser if it doesn't exist
if not User.objects.filter(email='admin@school.com').exists():
    User.objects.create_superuser(
        email='admin@school.com',
        password='admin123',
        first_name='Admin',
        last_name='User',
        role='ADMIN'
    )
    print("✓ Superuser created successfully!")
    print("  Email: admin@school.com")
    print("  Password: admin123")
else:
    print("✓ Superuser already exists")
    print("  Email: admin@school.com")
    print("  Password: admin123")
