from rest_framework import serializers
from .models import ClassRoom, Subject, Period, Timetable


class ClassRoomSerializer(serializers.ModelSerializer):
    class_teacher_name = serializers.CharField(source='class_teacher.get_full_name', read_only=True)
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = ClassRoom
        fields = '__all__'

    def get_student_count(self, obj):
        return obj.students.count() if hasattr(obj, 'students') else 0


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'


class TimetableSerializer(serializers.ModelSerializer):
    classroom_name = serializers.CharField(source='classroom.__str__', read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    teacher_name = serializers.CharField(source='teacher.get_full_name', read_only=True)
    period_time = serializers.SerializerMethodField()

    class Meta:
        model = Timetable
        fields = '__all__'

    def get_period_time(self, obj):
        return f"{obj.period.start_time.strftime('%H:%M')} - {obj.period.end_time.strftime('%H:%M')}"


class TimetableDetailSerializer(serializers.ModelSerializer):
    classroom = ClassRoomSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)
    teacher = serializers.SerializerMethodField()
    period = PeriodSerializer(read_only=True)

    class Meta:
        model = Timetable
        fields = '__all__'

    def get_teacher(self, obj):
        if obj.teacher:
            return {
                'id': obj.teacher.id,
                'name': obj.teacher.get_full_name(),
                'employee_id': obj.teacher.employee_id
            }
        return None
