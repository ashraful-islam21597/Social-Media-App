from django.contrib.auth.models import User
from django.db import models

from Users.models import CustomUser
from networks.models import Connection


class ChatRoom(models.Model):
    name = models.CharField(max_length=128)
    user=models.ManyToManyField(CustomUser)
    notification=models.BooleanField(default=False)
    last=models.CharField(max_length=120)
    #connection=models.ForeignKey(Connection,on_delete=models.CASCADE)

class Chat(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(to=ChatRoom, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.timestamp}]'

class chatroom_notification(models.Model):
    chatroom=models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    warning=models.BooleanField(default=False)