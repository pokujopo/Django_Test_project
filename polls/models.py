from django.db import models

# Create your models here.

class room(models.Model):
    user = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)


class Post(models.Model):

    image = models.ImageField(upload_to='images/', null=True, blank=True)

    video = models.FileField(upload_to='videos/', null=True, blank=True)