from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Cat(models.Model):
    image = models.ImageField(upload_to='portfolio/images/')
    name = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
