from django.views.generic.list import ListView
from api.models import Notifications, Student, Gallery


class NotificationListView(ListView):

    model = Notifications
    template_name = 'notifications.html'
    context_object_name = 'notifications'


class StudentListView(ListView):

    model = Student
    template_name = 'students.html'
    context_object_name = 'students'


class GalleryListView(ListView):

    model = Gallery
    template_name = 'gallery.html'
    context_object_name = 'gallery'






