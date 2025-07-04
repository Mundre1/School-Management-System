"""
Authentication Signals
Django signals for email notifications and user events
Professional signal patterns from Code IT internship
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import User, PasswordResetToken
from django.template.loader import render_to_string


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    """Send welcome email to new users"""
    if created and not instance.is_superuser:
        subject = 'Welcome to Smart School ERP System'
        message = f"""
        Dear {instance.get_full_name()},
        
        Welcome to Smart School ERP System!
        
        Your account has been successfully created with the following details:
        Email: {instance.email}
        Role: {instance.get_role_display()}
        
        Please verify your email address by clicking the link below:
        {settings.FRONTEND_URL}/verify-email/{instance.email_verification_token}
        
        If you have any questions, please contact our support team.
        
        Best regards,
        Smart School ERP Team
        """
        
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [instance.email],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Error sending welcome email: {e}")


@receiver(post_save, sender=PasswordResetToken)
def send_password_reset_email(sender, instance, created, **kwargs):
    """Send password reset email"""
    if created:
        subject = 'Password Reset Request - Smart School ERP'
        message = f"""
        Dear {instance.user.get_full_name()},
        
        You have requested to reset your password for Smart School ERP System.
        
        Please click the link below to reset your password:
        {settings.FRONTEND_URL}/reset-password/{instance.token}
        
        This link will expire in 24 hours.
        
        If you did not request this password reset, please ignore this email.
        
        Best regards,
        Smart School ERP Team
        """
        
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [instance.user.email],
                fail_silently=True,
            )
        except Exception as e:
            print(f"Error sending password reset email: {e}")
