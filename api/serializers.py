from rest_framework import serializers
from accounts.models import CustomUser
from api.models import Notifications, ContactMessages


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




