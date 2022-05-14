from django.contrib import admin
from api.models import ContactMessages, Notifications

# Register your models here.
admin.site.register(ContactMessages)
admin.site.register(Notifications)