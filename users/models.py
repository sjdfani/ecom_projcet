from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


class Gender(models.TextChoices):
    MALE = ('male', 'Male')
    FEMALE = ('female', 'Female')
    NONE = ('none', 'None')


class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_("email address"), unique=True)
    fullname = models.CharField(
        max_length=50, verbose_name=_('Fullname'), null=True, blank=True)
    home = models.CharField(
        max_length=11, verbose_name=_('Home'), null=True, blank=True)
    phone = models.CharField(
        max_length=11, verbose_name=_('Phone'), null=True, blank=True
    )
    national_code = models.CharField(
        max_length=20, verbose_name=_('National code'), null=True, blank=True)
    birthdate = models.DateTimeField(
        verbose_name=_('Birthdate'), null=True, blank=True)

    address = models.TextField(
        verbose_name=_('Address'), null=True, blank=True)
    gender = models.CharField(
        max_length=6, choices=Gender.choices, default=Gender.NONE, verbose_name=_('Gender'))
    get_newsletter = models.BooleanField(
        default=False, verbose_name=_('Get the newsletter'), null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Updated at'))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
