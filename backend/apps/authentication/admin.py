"""
Authentication Admin Configuration
Professional Django admin customization
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, OTP, PasswordResetToken, LoginHistory


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Custom User Admin"""
    
    list_display = ['email', 'get_full_name', 'role', 'is_active', 'email_verified', 'date_joined']
    list_filter = ['role', 'is_active', 'email_verified', 'gender', 'date_joined']
    search_fields = ['email', 'first_name', 'last_name', 'phone']
    ordering = ['-date_joined']
    
    fieldsets = (
        ('Authentication', {
            'fields': ('email', 'password')
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'middle_name', 'date_of_birth', 
                      'gender', 'profile_picture', 'bio', 'blood_group')
        }),
        ('Contact Information', {
            'fields': ('phone', 'emergency_contact', 'address', 'city', 
                      'state', 'country', 'postal_code')
        }),
        ('Permissions', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 
                      'groups', 'user_permissions')
        }),
        ('Email Verification', {
            'fields': ('email_verified', 'email_verification_token')
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 
                      'last_name', 'role', 'is_active'),
        }),
    )
    
    readonly_fields = ['date_joined', 'last_login']


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    """OTP Admin"""
    
    list_display = ['phone', 'otp_code', 'user', 'is_verified', 'created_at', 'expires_at']
    list_filter = ['is_verified', 'created_at']
    search_fields = ['phone', 'user__email']
    ordering = ['-created_at']
    readonly_fields = ['created_at']


@admin.register(PasswordResetToken)
class PasswordResetTokenAdmin(admin.ModelAdmin):
    """Password Reset Token Admin"""
    
    list_display = ['user', 'token', 'is_used', 'created_at', 'expires_at']
    list_filter = ['is_used', 'created_at']
    search_fields = ['user__email', 'token']
    ordering = ['-created_at']
    readonly_fields = ['created_at']


@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    """Login History Admin"""
    
    list_display = ['user', 'ip_address', 'is_successful', 'login_time', 'logout_time']
    list_filter = ['is_successful', 'login_time']
    search_fields = ['user__email', 'ip_address']
    ordering = ['-login_time']
    readonly_fields = ['login_time']
