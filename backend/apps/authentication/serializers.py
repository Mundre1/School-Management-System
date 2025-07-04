"""
Authentication Serializers
JWT-based authentication with DRF
Professional serializer patterns from Code IT internship
"""

from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, OTP, PasswordResetToken, LoginHistory
from django.utils import timezone
from datetime import timedelta
import random
import uuid


class UserSerializer(serializers.ModelSerializer):
    """User serializer for profile data"""
    
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id', 'email', 'phone', 'first_name', 'last_name', 'middle_name',
            'full_name', 'date_of_birth', 'gender', 'profile_picture',
            'address', 'city', 'state', 'country', 'postal_code',
            'role', 'is_active', 'email_verified', 'date_joined',
            'bio', 'emergency_contact', 'blood_group'
        ]
        read_only_fields = ['id', 'date_joined', 'email_verified']
    
    def get_full_name(self, obj):
        return obj.get_full_name()


class RegisterSerializer(serializers.ModelSerializer):
    """User registration serializer"""
    
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    
    class Meta:
        model = User
        fields = [
            'email', 'password', 'password_confirm', 'first_name',
            'last_name', 'middle_name', 'phone', 'date_of_birth',
            'gender', 'role'
        ]
    
    def validate(self, attrs):
        """Validate password match"""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                "password": "Password fields didn't match."
            })
        return attrs
    
    def validate_email(self, value):
        """Validate email uniqueness"""
        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError("User with this email already exists.")
        return value.lower()
    
    def create(self, validated_data):
        """Create new user"""
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        
        # Generate email verification token
        validated_data['email_verification_token'] = str(uuid.uuid4())
        
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        
        # TODO: Send verification email
        
        return user


class LoginSerializer(serializers.Serializer):
    """User login serializer with JWT tokens"""
    
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )
    
    def validate(self, attrs):
        """Authenticate user and return tokens"""
        email = attrs.get('email', '').lower()
        password = attrs.get('password')
        
        if not email or not password:
            raise serializers.ValidationError('Must include "email" and "password".')
        
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        
        if not user:
            raise serializers.ValidationError('Invalid email or password.')
        
        if not user.is_active:
            raise serializers.ValidationError('User account is disabled.')
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        
        attrs['user'] = user
        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)
        
        return attrs


class OTPLoginSerializer(serializers.Serializer):
    """Phone OTP login serializer"""
    
    phone = serializers.CharField(required=True)
    otp_code = serializers.CharField(required=True, max_length=6)
    
    def validate(self, attrs):
        """Validate OTP and return tokens"""
        phone = attrs.get('phone')
        otp_code = attrs.get('otp_code')
        
        try:
            otp = OTP.objects.filter(
                phone=phone,
                otp_code=otp_code,
                is_verified=False
            ).latest('created_at')
        except OTP.DoesNotExist:
            raise serializers.ValidationError('Invalid OTP code.')
        
        if otp.is_expired():
            raise serializers.ValidationError('OTP has expired.')
        
        # Mark OTP as verified
        otp.is_verified = True
        otp.save()
        
        user = otp.user
        
        if not user.is_active:
            raise serializers.ValidationError('User account is disabled.')
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        
        attrs['user'] = user
        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)
        
        return attrs


class SendOTPSerializer(serializers.Serializer):
    """Send OTP to phone number"""
    
    phone = serializers.CharField(required=True)
    
    def validate_phone(self, value):
        """Validate phone number exists"""
        try:
            user = User.objects.get(phone=value)
        except User.DoesNotExist:
            raise serializers.ValidationError('No user found with this phone number.')
        return value
    
    def create(self, validated_data):
        """Generate and send OTP"""
        phone = validated_data['phone']
        user = User.objects.get(phone=phone)
        
        # Generate 6-digit OTP
        otp_code = str(random.randint(100000, 999999))
        
        # Create OTP instance
        from django.conf import settings
        expires_at = timezone.now() + timedelta(minutes=settings.OTP_EXPIRY_MINUTES)
        
        otp = OTP.objects.create(
            user=user,
            phone=phone,
            otp_code=otp_code,
            expires_at=expires_at
        )
        
        # TODO: Send OTP via SMS (Twilio integration)
        # For development, return OTP in response
        
        return otp


class PasswordResetRequestSerializer(serializers.Serializer):
    """Request password reset"""
    
    email = serializers.EmailField(required=True)
    
    def validate_email(self, value):
        """Validate email exists"""
        try:
            user = User.objects.get(email=value.lower())
        except User.DoesNotExist:
            raise serializers.ValidationError('No user found with this email.')
        return value.lower()
    
    def create(self, validated_data):
        """Generate password reset token"""
        email = validated_data['email']
        user = User.objects.get(email=email)
        
        # Generate reset token
        token = str(uuid.uuid4())
        expires_at = timezone.now() + timedelta(hours=24)
        
        reset_token = PasswordResetToken.objects.create(
            user=user,
            token=token,
            expires_at=expires_at
        )
        
        # TODO: Send reset email with token
        
        return reset_token


class PasswordResetConfirmSerializer(serializers.Serializer):
    """Confirm password reset with token"""
    
    token = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    password_confirm = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )
    
    def validate(self, attrs):
        """Validate token and password match"""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                "password": "Password fields didn't match."
            })
        
        token = attrs.get('token')
        
        try:
            reset_token = PasswordResetToken.objects.get(token=token)
        except PasswordResetToken.DoesNotExist:
            raise serializers.ValidationError('Invalid reset token.')
        
        if not reset_token.is_valid:
            raise serializers.ValidationError('Reset token has expired or been used.')
        
        attrs['reset_token'] = reset_token
        return attrs
    
    def save(self):
        """Reset user password"""
        reset_token = self.validated_data['reset_token']
        password = self.validated_data['password']
        
        user = reset_token.user
        user.set_password(password)
        user.save()
        
        # Mark token as used
        reset_token.is_used = True
        reset_token.save()
        
        return user


class ChangePasswordSerializer(serializers.Serializer):
    """Change password for authenticated user"""
    
    old_password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )
    new_password = serializers.CharField(
        required=True,
        write_only=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )
    new_password_confirm = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )
    
    def validate(self, attrs):
        """Validate passwords"""
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError({
                "new_password": "Password fields didn't match."
            })
        return attrs
    
    def validate_old_password(self, value):
        """Validate old password"""
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Old password is incorrect.')
        return value
    
    def save(self):
        """Update user password"""
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


class EmailVerificationSerializer(serializers.Serializer):
    """Email verification serializer"""
    
    token = serializers.CharField(required=True)
    
    def validate_token(self, value):
        """Validate verification token"""
        try:
            user = User.objects.get(email_verification_token=value)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid verification token.')
        
        if user.email_verified:
            raise serializers.ValidationError('Email already verified.')
        
        return value
    
    def save(self):
        """Verify user email"""
        token = self.validated_data['token']
        user = User.objects.get(email_verification_token=token)
        user.email_verified = True
        user.email_verification_token = None
        user.save()
        return user


class LoginHistorySerializer(serializers.ModelSerializer):
    """Login history serializer"""
    
    user_email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = LoginHistory
        fields = [
            'id', 'user_email', 'ip_address', 'user_agent',
            'login_time', 'logout_time', 'is_successful'
        ]
        read_only_fields = fields
