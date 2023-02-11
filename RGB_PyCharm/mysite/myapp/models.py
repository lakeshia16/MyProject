from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Image(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='images/')
    url_img = models.FileField(upload_to='books/')
    coord = models.CharField(max_length=100)

    def __str__(self):
        return self.title

