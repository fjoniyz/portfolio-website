from django.db import models

class Project(models.Model):
    titel = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=150)

    def __str__(self):
        return self.titel
# Create your models here.
