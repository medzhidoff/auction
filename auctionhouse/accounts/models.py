from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import forms
import datetime

# Create your models here.

class Profile(models.Model):
    # if user is deleted, then delete profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='images_profiles')
    dob = models.DateField(max_length=8, default=datetime.date.today)
    name = models.CharField(null=True, max_length=40, blank=False)
    surname = models.CharField(null=True, max_length=40, blank=False)
    patronymic = models.CharField(null=True, max_length=40, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    #override save method
    def save(self, *args, **kwargs):
        # call parent save method
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
