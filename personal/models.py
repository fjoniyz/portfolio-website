from django.db import models

class Project(models.Model):
    titel = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=150)
# Create your models here.
