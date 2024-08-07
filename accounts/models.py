from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse


class UserManager(BaseUserManager):
    def create_user(self, email: str = None, password: str = None, **other_fields):
        other_fields.setdefault("is_active", True)

        if not email and other_fields.get('is_superuser'):
            email = "{}@django.com".format(other_fields.get('username'))

        user = User(email=email, password=password, **other_fields)

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_superuser(self, email: str = None, password: str = None, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault("is_active", True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(email, password, **other_fields)


class User(AbstractUser):
    # remove default fields
    name = None
    # bio = models.TextField("Bio", blank=True, null=True)
    # image = models.ImageField("Profile Image", upload_to="users/", default="users/default.png", blank=True, null=True)

    email = models.EmailField("Email Address", unique=True)
    username = models.CharField("Username", max_length=150, unique=True)
    password = models.CharField("Password", max_length=128)

    create_at = models.DateTimeField("Create At", auto_now_add=True)
    update_at = models.DateTimeField("Update At", auto_now=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        return reverse("profile", args=[self.id])

    def get_full_name(self) -> str:
        return self.username

    def get_short_name(self) -> str:
        return self.username
