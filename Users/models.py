from datetime import date

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    contact = models.TextField(max_length=15)
    DOB = models.DateField(blank=True, null=True)
    confirm_password = models.TextField(max_length=120)

    def __str__(self):
        return self.username


class profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    contact = models.CharField(max_length=11)
    address = models.TextField(max_length=120, null=True, blank=True)
    Home = models.TextField(max_length=120, null=True, blank=True)

    #profilepicture = models.ImageField(upload_to='profilepicture', default='no_pic.png')
    #cover_picture = models.ImageField(upload_to='coverpicture', default='no_cover_pic.png')
    profilepicture = CloudinaryField('MyBuddy/profilepicture')
    cover_picture = CloudinaryField('MyBuddy/coverpicture')

    # coverpicture = CloudinaryField('image')
    #profilepicture_url = models.CharField(max_length=400)
    active_status = models.TextField(max_length=5)
    # def proffession(self):
    #     return self.profession_set.get(profession)

    def Fullname(self):
        return f' {self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})


class Graduate_school(models.Model):
    profile = models.ForeignKey(profile, on_delete=models.CASCADE)
    Graduate_school_name = models.CharField(max_length=120,null=True,blank=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    @property
    def current_date(self):
        return date.today()


class college(models.Model):
    profile = models.ForeignKey(profile, on_delete=models.CASCADE)
    college = models.CharField(max_length=120,null=True,blank=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    @property
    def current_date(self):
        return date.today()


class school(models.Model):
    profile = models.ForeignKey(profile, on_delete=models.CASCADE)
    school = models.CharField(max_length=120,null=True,blank=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    @property
    def current_date(self):
        return date.today()


class profession(models.Model):
    profile = models.ForeignKey(profile, on_delete=models.CASCADE)
    profession = models.CharField(max_length=120,null=True,blank=True)
    company = models.CharField(max_length=120,null=True,blank=True)


class social_link(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Facebook = models.URLField(max_length=220, null=True, blank=True)
    Instragram = models.URLField(max_length=220, null=True, blank=True)
    Linkedin = models.URLField(max_length=220, null=True, blank=True)
    Twitter = models.URLField(max_length=220, null=True, blank=True)
    Github = models.URLField(max_length=220, null=True, blank=True)
