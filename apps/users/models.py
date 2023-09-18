from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.users.manager import CustomUserManager


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/avatars/', blank=True, null=True, verbose_name='Profiles_avatar')
    verify_code = models.CharField(max_length=6, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email