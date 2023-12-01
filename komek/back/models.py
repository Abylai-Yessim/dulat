from django.db import models
import uuid
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'images/{new_file_name}'

class Organ(models.Model):
    title = models.CharField(max_length=100, default="Default Title")
    description = models.TextField(default="")  


    def __str__(self):
        return self.title

class Notification(models.Model):
    name = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100, default="")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.organ.title} Notification"


