from django.db import models

# Create your models here.

class Insect(models.Model):
    name = models.CharField(max_length=200)
    timeframe = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Fish(models.Model):
    name = models.CharField(max_length=200)
    shadow = models.CharField(max_length=200)
    timeframe = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class NorthMonth(models.Model):
    name = models.CharField(max_length=200)
    season = models.CharField(max_length=200)
    fish = models.ManyToManyField(Fish)
    insect = models.ManyToManyField(Insect)

    def __str__(self):
        return self.name

class SouthMonth(models.Model):
    name = models.CharField(max_length=200)
    season = models.CharField(max_length=200)
    fish = models.ManyToManyField(Fish)
    insect = models.ManyToManyField(Insect)

    def __str__(self):
        return self.name