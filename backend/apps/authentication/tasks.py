"""
Celery Tasks for Authentication
Async tasks for email sending and OTP cleanup
"""

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import OTP


@shared_task
def send_welcome_email_task(user_id):
    """Send welcome email asynchronously"""
    from .models import User
    
    try:
        user = User.objects.get(id=user_id)
        subject = 'Welcome to Smart School ERP System'
        message = f"""
        Dear {user.get_full_name()},
        
        Welcome to Smart School ERP System!
        
        Your account has been successfully created.
        
        Best regards,
        Smart School ERP Team
        """
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        return f"Welcome email sent to {user.email}"
    except Exception as e:
        return f"Error sending welcome email: {str(e)}"


@shared_task
def send_otp_sms_task(phone, otp_code):
    """Send OTP via SMS asynchronously"""
    # TODO: Implement Twilio SMS sending
    try:
        # Twilio implementation here
        print(f"Sending OTP {otp_code} to {phone}")
        return f"OTP sent to {phone}"
    except Exception as e:
        return f"Error sending OTP: {str(e)}"


@shared_task
def cleanup_expired_otps():
    """Clean up expired OTPs"""
    try:
        expired_otps = OTP.objects.filter(
            expires_at__lt=timezone.now(),
            is_verified=False
        )
        count = expired_otps.count()
        expired_otps.delete()
        return f"Deleted {count} expired OTPs"
    except Exception as e:
        return f"Error cleaning up OTPs: {str(e)}"


@shared_task
def send_password_reset_email_task(user_id, reset_token):
    """Send password reset email asynchronously"""
    from .models import User
    
    try:
        user = User.objects.get(id=user_id)
        subject = 'Password Reset Request - Smart School ERP'
        message = f"""
        Dear {user.get_full_name()},
        
        You have requested to reset your password.
        
        Please click the link below to reset your password:
        {settings.FRONTEND_URL}/reset-password/{reset_token}
        
        This link will expire in 24 hours.
        
        Best regards,
        Smart School ERP Team
        """
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        return f"Password reset email sent to {user.email}"
    except Exception as e:
        return f"Error sending password reset email: {str(e)}"
