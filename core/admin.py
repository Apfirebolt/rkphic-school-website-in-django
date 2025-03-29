from django.contrib import admin
from . models import Student, Teacher, Notification, Class, Attendance, Exam, Result

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Notification)
admin.site.register(Class)
admin.site.register(Attendance)
admin.site.register(Exam)
admin.site.register(Result)


