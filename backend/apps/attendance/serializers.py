from rest_framework import serializers
from .models import Attendance
from apps.students.serializers import StudentSerializer


class AttendanceSerializer(serializers.ModelSerializer):
    student_details = StudentSerializer(source='student', read_only=True)
    
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ['marked_at']


class BulkAttendanceSerializer(serializers.Serializer):
    date = serializers.DateField()
    attendances = serializers.ListField(
        child=serializers.DictField()
    )
