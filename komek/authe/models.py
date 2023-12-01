from django.db import models
import uuid
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'avatars/{new_file_name}'

# Create your models here.

class CustomUser(AbstractUser):
    lastname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=uniq_name_upload, blank=True, null=True)

    def __str__(self):
        return self.user.username



