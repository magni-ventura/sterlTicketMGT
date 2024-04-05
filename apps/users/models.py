import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


# Create your models here.
#User model
class User(AbstractBaseUser, PermissionsMixin):
     pkid = models.BigAutoField(primary_key=True, editable=False)
     
     id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

     username = models.CharField(verbose_name=_("Username"), max_length=255, unique=True)
     
     first_name = models.CharField(verbose_name=_("First Name"), max_length=50)
     
     last_name = models.CharField(verbose_name=_("Last Name"), max_length=50)
     
     email = models.EmailField(verbose_name=_("Email Address"), unique=True)
     
     is_staff = models.BooleanField(default=True)
     
     is_active = models.BooleanField(default=True)
     date_joined = models.DateTimeField(default=timezone.now)

     #Username field the name of the user and  is set to the email address of the user
     USERNAME_FIELD = "email"
     REQUIRED_FIELDS = ["username", "first_name", "last_name"]
     #Objects of the user manager
     objects = CustomUserManager()


     class Meta:
          verbose_name= _("User")
          verbose_name_plural=("Users")

     #String representation
     def __str__(self):
          return self.username

     #Set the properties of the user manager
     @property
     def get_full_name(self):
          return f"{self.first_name.title()}{self.last_name.title()}"

     #Function to get the short user name
     def get_short_name  (self):
          return self.username
