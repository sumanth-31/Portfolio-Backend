from django.db import models
from rest.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
