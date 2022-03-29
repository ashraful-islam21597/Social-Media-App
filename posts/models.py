from cloudinary.models import CloudinaryField
from django.db import models

from Users.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.TextField(max_length=3000,blank=True, null=True)
    post_image = CloudinaryField('MyBuddy/timelinepicture', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    audiance = models.IntegerField(choices=((1, ("Public")),
                                            (2, ("Friends")),
                                            (3, ("Only me"))),
                                   default=1)

    def __str__(self):
        return f'{self.user.username}--{self.status}'


class Post_reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    total_react = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.post.status


class Reaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_reaction = models.ForeignKey(Post_reaction, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    react = models.BooleanField(default=False)

class Comment(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.TextField(max_length=2000)
    picture=models.ImageField(upload_to='comment',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    reply=models.TextField(max_length=2000)
    picture=models.ImageField(upload_to='comment',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

