from django.contrib import admin
from .models import Notice, Message, Notification


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'target_audience', 'created_by', 'published_at', 'is_active']
    list_filter = ['priority', 'target_audience', 'is_active', 'published_at']
    search_fields = ['title', 'content']
    ordering = ['-published_at']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'sender', 'recipient', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['subject', 'body', 'sender__email', 'recipient__email']
    ordering = ['-created_at']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'notification_type', 'is_read', 'created_at']
    list_filter = ['notification_type', 'is_read', 'created_at']
    search_fields = ['title', 'message', 'user__email']
    ordering = ['-created_at']
