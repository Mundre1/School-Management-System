from rest_framework import serializers
from .models import LeaveApplication


class LeaveApplicationSerializer(serializers.ModelSerializer):
    applicant_name = serializers.CharField(read_only=True)
    total_days = serializers.IntegerField(read_only=True)
    approved_by_name = serializers.CharField(source='approved_by.get_full_name', read_only=True)

    class Meta:
        model = LeaveApplication
        fields = '__all__'

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date")
        return data
