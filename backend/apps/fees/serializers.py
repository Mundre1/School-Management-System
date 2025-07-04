from rest_framework import serializers
from .models import FeeStructure, FeePayment
from apps.students.serializers import StudentSerializer


class FeeStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeStructure
        fields = '__all__'
        read_only_fields = ['total_fee', 'created_at', 'updated_at']


class FeePaymentSerializer(serializers.ModelSerializer):
    student_details = StudentSerializer(source='student', read_only=True)
    fee_structure_details = FeeStructureSerializer(source='fee_structure', read_only=True)
    
    class Meta:
        model = FeePayment
        fields = '__all__'
        read_only_fields = ['amount_remaining', 'created_at', 'updated_at']
