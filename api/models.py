from django.db import models
from rkphic_school.settings import AUTH_USER_MODEL


class ContactMessages(models.Model):
    sender_name = models.CharField("Sender Name", max_length=200)
    sender_email = models.EmailField("Sender Email", max_length=200)
    subject = models.CharField("Sender Subject", max_length=200)
    message = models.TextField()

    def __str__(self):
        return str(self.sender_name) + '-' + str(self.sender_email)

    class Meta:
        verbose_name_plural = "Contact Messages"


class Notifications(models.Model):
    created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subtitle = models.TextField(null=True, blank=True)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.title) + '-' + str(self.subtitle)

    class Meta:
        verbose_name_plural = "Notifications"


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = "Students"


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Gallery"






