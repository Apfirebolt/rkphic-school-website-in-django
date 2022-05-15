from django.contrib import admin
from api.models import ContactMessages, Notifications, Gallery, Student

# Register your models here.
admin.site.register(ContactMessages)
admin.site.register(Notifications)
admin.site.register(Gallery)
admin.site.register(Student)