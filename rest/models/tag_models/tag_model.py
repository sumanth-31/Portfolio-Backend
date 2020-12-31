from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
