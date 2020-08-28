from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django.urls import reverse


class CustomUser(AbstractUser):
    display_name = models.CharField(max_length = 50, null=True)


    REQUIRED_FIELDS = ['display_name']

    def __str__(self):
        return self.username


class Tickets(models.Model):
    CHOICES = (("New", 'New'), ("In Progress", "In Progress"), ("Done", "Done"), ("Invalid", "Invalid"))
    status = models.CharField(max_length=200, null=True, choices=CHOICES, default="New")
    title = models.CharField(max_length=200, null=True)
    filer = models.ForeignKey(CustomUser, related_name="custom_user_profile", null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    timestamp = models.DateTimeField(default=now, editable=False)
    assignee = models.ForeignKey(CustomUser, related_name="assignee_profile", null=True, on_delete=models.SET_NULL, blank=True, default=None)
    completer = models.ForeignKey(CustomUser, related_name="completer_profile", null=True, on_delete=models.SET_NULL, blank=True, default=None)

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.pk})
