from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

from rest_framework_simplejwt.tokens import RefreshToken
from .user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_pic = models.ImageField(blank=True)
    resume = models.FileField(blank=True)
    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self.__generate_token()

    def __generate_token(self):
        token = RefreshToken.for_user(self)
        return str(token.access_token)
