from rest_framework import serializers
from accounts.models import CustomUser
from api.models import Notifications, ContactMessages
from core.models import Student, Teacher


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_staff', 'password')

    def create(self, validated_data):
        user = super(CustomUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notifications
        fields = '__all__'


class ContactMessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactMessages
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'age',
            'email',
            'phone_number',
            'address',
            'roll_number',
            'enrollment_date',
            'current_class',
            'guardian_name',
            'guardian_contact',
            'guardian_relationship',
            'emergency_contact'
        ]

class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
            'hire_date',
            'salary',
            'subject',
        ]
        read_only_fields = ['hire_date']
        extra_kwargs = {
            'salary': {'required': True},
            'subject': {'required': True},
        }




