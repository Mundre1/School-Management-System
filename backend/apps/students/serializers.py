"""
Student Serializers
DRF serializers for student management API
"""

from rest_framework import serializers
from apps.authentication.serializers import UserSerializer
from .models import Student, Guardian, StudentDocument, StudentNote, StudentAchievement


class GuardianSerializer(serializers.ModelSerializer):
    """Serializer for Guardian model"""
    
    class Meta:
        model = Guardian
        fields = [
            'id', 'student', 'name', 'relation', 'phone', 'email',
            'occupation', 'address', 'is_primary', 'is_emergency_contact',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class StudentDocumentSerializer(serializers.ModelSerializer):
    """Serializer for Student Document model"""
    
    uploaded_by_name = serializers.CharField(source='uploaded_by.get_full_name', read_only=True)
    
    class Meta:
        model = StudentDocument
        fields = [
            'id', 'student', 'document_type', 'document_name', 'document_file',
            'description', 'uploaded_by', 'uploaded_by_name', 'uploaded_at', 'updated_at'
        ]
        read_only_fields = ['id', 'uploaded_at', 'updated_at', 'uploaded_by_name']


class StudentNoteSerializer(serializers.ModelSerializer):
    """Serializer for Student Note model"""
    
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    
    class Meta:
        model = StudentNote
        fields = [
            'id', 'student', 'note_type', 'title', 'content',
            'created_by', 'created_by_name', 'is_private',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by_name']


class StudentAchievementSerializer(serializers.ModelSerializer):
    """Serializer for Student Achievement model"""
    
    recorded_by_name = serializers.CharField(source='recorded_by.get_full_name', read_only=True)
    
    class Meta:
        model = StudentAchievement
        fields = [
            'id', 'student', 'achievement_type', 'title', 'description',
            'date_achieved', 'certificate', 'awarded_by', 'recorded_by',
            'recorded_by_name', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'recorded_by_name']


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student model"""
    
    user = UserSerializer(read_only=True)
    user_id = serializers.UUIDField(write_only=True, required=False)
    full_class = serializers.CharField(read_only=True)
    age = serializers.IntegerField(read_only=True)
    guardians = GuardianSerializer(many=True, read_only=True)
    
    class Meta:
        model = Student
        fields = [
            'id', 'user', 'user_id', 'admission_number', 'roll_number',
            'class_name', 'section', 'academic_year', 'full_class',
            'admission_date', 'admission_type', 'previous_school',
            'status', 'age',
            'father_name', 'father_phone', 'father_email', 'father_occupation',
            'mother_name', 'mother_phone', 'mother_email', 'mother_occupation',
            'medical_conditions', 'allergies',
            'birth_certificate', 'transfer_certificate',
            'guardians', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'full_class', 'age']
    
    def create(self, validated_data):
        """Create student with user_id"""
        user_id = validated_data.pop('user_id', None)
        if user_id:
            from apps.authentication.models import User
            validated_data['user'] = User.objects.get(id=user_id)
        return super().create(validated_data)


class StudentDetailSerializer(StudentSerializer):
    """Detailed serializer for Student with all related data"""
    
    documents = StudentDocumentSerializer(many=True, read_only=True)
    notes = StudentNoteSerializer(many=True, read_only=True)
    achievements = StudentAchievementSerializer(many=True, read_only=True)
    
    class Meta(StudentSerializer.Meta):
        fields = StudentSerializer.Meta.fields + ['documents', 'notes', 'achievements']


class StudentListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for student list"""
    
    student_name = serializers.CharField(source='user.get_full_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    phone = serializers.CharField(source='user.phone', read_only=True)
    full_class = serializers.CharField(read_only=True)
    age = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Student
        fields = [
            'id', 'admission_number', 'roll_number', 'student_name',
            'email', 'phone', 'class_name', 'section', 'full_class',
            'status', 'age', 'admission_date'
        ]


class StudentCreateSerializer(serializers.Serializer):
    """Serializer for creating student with user account"""
    
    # User fields
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    middle_name = serializers.CharField(max_length=100, required=False, allow_blank=True)
    date_of_birth = serializers.DateField()
    gender = serializers.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    phone = serializers.CharField(max_length=17, required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    city = serializers.CharField(max_length=100, required=False, allow_blank=True)
    blood_group = serializers.CharField(max_length=5, required=False, allow_blank=True)
    
    # Student fields
    admission_number = serializers.CharField(max_length=50)
    roll_number = serializers.CharField(max_length=50, required=False, allow_blank=True)
    class_name = serializers.CharField(max_length=50)
    section = serializers.CharField(max_length=10, required=False, allow_blank=True)
    academic_year = serializers.CharField(max_length=20)
    admission_date = serializers.DateField()
    admission_type = serializers.ChoiceField(
        choices=[('REGULAR', 'Regular'), ('TRANSFER', 'Transfer'), ('SCHOLARSHIP', 'Scholarship')],
        default='REGULAR'
    )
    previous_school = serializers.CharField(max_length=255, required=False, allow_blank=True)
    
    # Guardian fields
    father_name = serializers.CharField(max_length=200)
    father_phone = serializers.CharField(max_length=17, required=False, allow_blank=True)
    father_email = serializers.EmailField(required=False, allow_blank=True)
    father_occupation = serializers.CharField(max_length=100, required=False, allow_blank=True)
    
    mother_name = serializers.CharField(max_length=200)
    mother_phone = serializers.CharField(max_length=17, required=False, allow_blank=True)
    mother_email = serializers.EmailField(required=False, allow_blank=True)
    mother_occupation = serializers.CharField(max_length=100, required=False, allow_blank=True)
    
    # Medical fields
    medical_conditions = serializers.CharField(required=False, allow_blank=True)
    allergies = serializers.CharField(required=False, allow_blank=True)
    
    def validate_admission_number(self, value):
        """Check if admission number already exists"""
        if Student.objects.filter(admission_number=value).exists():
            raise serializers.ValidationError("Admission number already exists")
        return value
    
    def validate_email(self, value):
        """Check if email already exists"""
        from apps.authentication.models import User
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
    
    def create(self, validated_data):
        """Create user and student profile"""
        from apps.authentication.models import User
        
        # Extract user data
        user_data = {
            'email': validated_data['email'],
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
            'middle_name': validated_data.get('middle_name', ''),
            'date_of_birth': validated_data['date_of_birth'],
            'gender': validated_data['gender'],
            'phone': validated_data.get('phone', ''),
            'address': validated_data.get('address', ''),
            'city': validated_data.get('city', ''),
            'blood_group': validated_data.get('blood_group', ''),
            'role': 'STUDENT',
            'is_active': True,
        }
        
        # Create user
        user = User.objects.create_user(
            email=user_data['email'],
            password=validated_data['password'],
            **{k: v for k, v in user_data.items() if k != 'email'}
        )
        
        # Extract student data
        student_data = {
            'user': user,
            'admission_number': validated_data['admission_number'],
            'roll_number': validated_data.get('roll_number', ''),
            'class_name': validated_data['class_name'],
            'section': validated_data.get('section', ''),
            'academic_year': validated_data['academic_year'],
            'admission_date': validated_data['admission_date'],
            'admission_type': validated_data.get('admission_type', 'REGULAR'),
            'previous_school': validated_data.get('previous_school', ''),
            'father_name': validated_data['father_name'],
            'father_phone': validated_data.get('father_phone', ''),
            'father_email': validated_data.get('father_email', ''),
            'father_occupation': validated_data.get('father_occupation', ''),
            'mother_name': validated_data['mother_name'],
            'mother_phone': validated_data.get('mother_phone', ''),
            'mother_email': validated_data.get('mother_email', ''),
            'mother_occupation': validated_data.get('mother_occupation', ''),
            'medical_conditions': validated_data.get('medical_conditions', ''),
            'allergies': validated_data.get('allergies', ''),
        }
        
        # Create student
        student = Student.objects.create(**student_data)
        
        return student
