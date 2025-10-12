from rest_framework import serializers
from .models import Assignment, AssignmentSubmission


class AssignmentSerializer(serializers.ModelSerializer):
    classroom_name = serializers.CharField(source='classroom.__str__', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    teacher_name = serializers.CharField(source='teacher.get_full_name', read_only=True)
    is_overdue = serializers.BooleanField(read_only=True)
    submission_count = serializers.IntegerField(read_only=True)
    pending_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Assignment
        fields = '__all__'


class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    assignment_title = serializers.CharField(source='assignment.title', read_only=True)
    student_name = serializers.CharField(source='student.get_full_name', read_only=True)
    is_late = serializers.BooleanField(read_only=True)
    percentage = serializers.FloatField(read_only=True)
    graded_by_name = serializers.CharField(source='graded_by.get_full_name', read_only=True)

    class Meta:
        model = AssignmentSubmission
        fields = '__all__'

    def create(self, validated_data):
        from django.utils import timezone
        validated_data['submitted_at'] = timezone.now()
        validated_data['status'] = 'submitted'
        
        # Check if late
        assignment = validated_data['assignment']
        if timezone.now() > assignment.due_date:
            validated_data['status'] = 'late'
        
        return super().create(validated_data)
