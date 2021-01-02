from django.db import models
from rest.models import User

class Tag(models.Model):
    class Meta:
        constraints=[models.UniqueConstraint(fields=["name","user"],name="unique_user_tag")]
    name = models.CharField(max_length=20)
    image = models.ImageField(blank=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
