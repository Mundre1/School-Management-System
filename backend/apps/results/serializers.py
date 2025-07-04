from rest_framework import serializers
from .models import Exam, Subject, Result
from apps.students.serializers import StudentSerializer


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = ['created_at']


class ResultSerializer(serializers.ModelSerializer):
    student_details = StudentSerializer(source='student', read_only=True)
    exam_details = ExamSerializer(source='exam', read_only=True)
    subject_details = SubjectSerializer(source='subject', read_only=True)
    
    class Meta:
        model = Result
        fields = '__all__'
        read_only_fields = ['percentage', 'grade', 'created_at', 'updated_at']
