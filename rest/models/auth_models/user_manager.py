from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, name="User"):
        if email is None:
            raise TypeError("Users must have an email")
        if password is None:
            raise TypeError("Users must have a password")
        email = self.normalize_email(email)
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, name="SuperUser"):
        user = self.create_user(email, password, name)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
