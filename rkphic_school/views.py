from django.views.generic.list import ListView
from api.models import Notifications


class NotificationListView(ListView):

    model = Notifications
    template_name = 'notifications.html'
    context_object_name = 'notifications'





