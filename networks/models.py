from django.db import models

from Users.models import CustomUser, profile


class Network(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    sent_request = models.PositiveIntegerField(default=0)
    friend_request = models.PositiveIntegerField(default=0)
    total_connection = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username


class Connection(models.Model):
    connected = models.BooleanField(default=False)
    profiles = models.ForeignKey(profile, on_delete=models.CASCADE)
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    request_for_connection = models.BooleanField(default=False)
    sent_request_for_connection = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.profiles.user.username} following {self.network.user.username}'
