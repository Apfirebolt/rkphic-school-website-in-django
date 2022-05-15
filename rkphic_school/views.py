from django.views.generic.list import ListView
from api.models import Notifications, Student


class NotificationListView(ListView):

    model = Notifications
    template_name = 'notifications.html'
    context_object_name = 'notifications'


class StudentListView(ListView):

    model = Student
    template_name = 'students.html'
    context_object_name = 'students'






