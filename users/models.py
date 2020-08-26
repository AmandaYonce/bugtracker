from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    display_name = models.CharField(max_length =  50, null=True)
    age = models.IntegerField(null=True)


    REQUIRED_FIELDS = ['age', 'display_name']

    def __str__(self):
        return self.username