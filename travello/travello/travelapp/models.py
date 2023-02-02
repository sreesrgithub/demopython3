from django.db import models


# Create your models here
class Place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img')
    description = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):

    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image')
    about = models.TextField()

    def __str__(self):
        return self.name
