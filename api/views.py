from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from api.serializers import CustomUserSerializer, NotificationSerializer, ContactMessagesSerializer
from accounts.models import CustomUser
from api.models import Notifications, ContactMessages


class CreateCustomUserApiView(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class ChangeSettingsApiView(UpdateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj


class GetContactMessages(ListAPIView):
    serializer_class = ContactMessagesSerializer
    queryset = ContactMessages.objects.all()


class GetNotifications(ListAPIView):
    serializer_class = NotificationSerializer
    queryset = Notifications.objects.all()




