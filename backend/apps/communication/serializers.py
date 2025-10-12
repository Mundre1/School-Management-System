from rest_framework import serializers
from .models import Notice, Message, Notification


class NoticeSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    target_classroom_name = serializers.CharField(source='target_classroom.__str__', read_only=True)
    is_expired = serializers.BooleanField(read_only=True)

    class Meta:
        model = Notice
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.get_full_name', read_only=True)
    recipient_name = serializers.CharField(source='recipient.get_full_name', read_only=True)
    reply_count = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = '__all__'

    def get_reply_count(self, obj):
        return obj.replies.count()


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
