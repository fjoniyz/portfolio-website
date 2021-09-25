from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name
# Create your models here.
