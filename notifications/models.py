from django.db import models

from Users.models import CustomUser


class Notifications(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    notification_TYPE=models.IntegerField(default=0)
    text=models.TextField(max_length=120)
    notification_image=models.ImageField(upload_to='notifications',default='notification')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
