"""
Authentication URLs
JWT-based authentication endpoints
"""

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from .views import (
    RegisterView, LoginView, LogoutView, ProfileView,
    ChangePasswordView, PasswordResetRequestView, PasswordResetConfirmView,
    EmailVerificationView, SendOTPView, OTPLoginView, LoginHistoryView,
    check_auth
)

app_name = 'authentication'

urlpatterns = [
    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('check/', check_auth, name='check_auth'),
    
    # JWT Token Management
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    
    # User Profile
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('login-history/', LoginHistoryView.as_view(), name='login_history'),
    
    # Password Reset
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    # Email Verification
    path('verify-email/', EmailVerificationView.as_view(), name='verify_email'),
    
    # OTP Authentication
    path('send-otp/', SendOTPView.as_view(), name='send_otp'),
    path('otp-login/', OTPLoginView.as_view(), name='otp_login'),
]
