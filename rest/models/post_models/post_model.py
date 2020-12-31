from django.db import models
from rest.models import Collection, Tag, User


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_id = models.AutoField(primary_key=True)
    content = models.TextField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    privacy=models.CharField(max_length=20,default="public")