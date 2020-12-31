from django.contrib import admin

# Register your models here.
from .models import User, Post, Collection

admin.site.register(User)
admin.site.register(Collection)
admin.site.register(Post)
