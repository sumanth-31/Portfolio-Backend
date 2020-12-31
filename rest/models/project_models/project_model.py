from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(blank=True)
