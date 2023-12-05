from django.db import models
from django.contrib.auth.models import User  
import uuid

def uniq_name_upload(instance, filename):
    new_file_name = f"{uuid.uuid4()}.{filename.split('.')[-1]}"
    return f'images/{new_file_name}'

class Organ(models.Model):
    title = models.CharField(max_length=100, default="Default Title")
    description = models.TextField(default="")  

    def __str__(self):
        return self.title

class Notification(models.Model):
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=255) 
    description = models.CharField(max_length=255, default="")  
    phone_number = models.CharField(max_length=100, default="")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.organ.title}"

class Comment(models.Model):
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)