"""
Custom Permissions for Role-Based Access Control
Professional permission classes from Code IT internship
"""

from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Permission class for Admin (Head of School) only
    """
    message = 'Only administrators can perform this action.'
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'ADMIN'


class IsStaff(permissions.BasePermission):
    """
    Permission class for Staff/Teacher only
    """
    message = 'Only staff members can perform this action.'
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'STAFF'


class IsStudent(permissions.BasePermission):
    """
    Permission class for Student only
    """
    message = 'Only students can perform this action.'
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'STUDENT'


class IsAdminOrStaff(permissions.BasePermission):
    """
    Permission class for Admin or Staff
    """
    message = 'Only administrators or staff can perform this action.'
    
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['ADMIN', 'STAFF'])


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission class: Admin can edit, others can only read
    """
    message = 'Only administrators can modify this resource.'
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_authenticated and request.user.role == 'ADMIN'


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permission class: Owner or Admin can access
    """
    message = 'You do not have permission to access this resource.'
    
    def has_object_permission(self, request, view, obj):
        # Admin has full access
        if request.user.role == 'ADMIN':
            return True
        
        # Check if user is the owner
        if hasattr(obj, 'user'):
            return obj.user == request.user
        
        return obj == request.user


class IsOwnerOrStaffOrAdmin(permissions.BasePermission):
    """
    Permission class: Owner, Staff, or Admin can access
    """
    message = 'You do not have permission to access this resource.'
    
    def has_object_permission(self, request, view, obj):
        # Admin and Staff have full access
        if request.user.role in ['ADMIN', 'STAFF']:
            return True
        
        # Check if user is the owner
        if hasattr(obj, 'user'):
            return obj.user == request.user
        
        if hasattr(obj, 'student'):
            return obj.student.user == request.user
        
        return obj == request.user


class CanManageStudents(permissions.BasePermission):
    """
    Permission to manage students (Admin and Staff)
    """
    message = 'You do not have permission to manage students.'
    
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['ADMIN', 'STAFF'])


class CanManageStaff(permissions.BasePermission):
    """
    Permission to manage staff (Admin only)
    """
    message = 'Only administrators can manage staff.'
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'ADMIN'


class CanManageFees(permissions.BasePermission):
    """
    Permission to manage fees (Admin only)
    """
    message = 'Only administrators can manage fees.'
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_authenticated and request.user.role == 'ADMIN'


class CanManageResults(permissions.BasePermission):
    """
    Permission to manage results (Admin and Staff)
    """
    message = 'You do not have permission to manage results.'
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['ADMIN', 'STAFF'])


class CanManageAttendance(permissions.BasePermission):
    """
    Permission to manage attendance (Admin and Staff)
    """
    message = 'You do not have permission to manage attendance.'
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['ADMIN', 'STAFF'])
