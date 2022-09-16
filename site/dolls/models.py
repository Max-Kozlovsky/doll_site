from django.db import models


# Create your models here.
class InteriorDolls(models.Model):
    name = models.CharField(max_length=50)
    available = models.CharField(max_length=30)
    description = models.TextField()
    price = models.CharField(max_length=20)
    image = models.FileField(upload_to='static/img/')

    def __str__(self):
        return self.name


class PlayDolls(models.Model):
    name = models.CharField(max_length=50)
    available = models.CharField(max_length=30)
    description = models.TextField()
    price = models.CharField(max_length=20)
    image = models.FileField(upload_to='static/img/')

    def __str__(self):
        return self.name


class Toys(models.Model):
    name = models.CharField(max_length=50)
    available = models.CharField(max_length=30)
    description = models.TextField()
    price = models.CharField(max_length=20)
    image = models.FileField(upload_to='static/img/')

    def __str__(self):
        return self.name


class DollsDress(models.Model):
    name = models.CharField(max_length=50)
    available = models.CharField(max_length=30)
    description = models.TextField()
    price = models.CharField(max_length=20)
    image = models.FileField(upload_to='static/img/')

    def __str__(self):
        return self.name


class ToysDress(models.Model):
    name = models.CharField(max_length=50)
    available = models.CharField(max_length=30)
    description = models.TextField()
    price = models.CharField(max_length=20)
    image = models.FileField(upload_to='static/img/')

    def __str__(self):
        return self.name
