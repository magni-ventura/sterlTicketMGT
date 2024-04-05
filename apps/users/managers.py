from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

#Base user manager
#The Underscore_ is meant for translation if need be
class CustomUserManager(BaseUserManager):
    #Validate email
    def email_validator(self, email):
        try:
            #validate email
            validate_email(email)
        #Raise a Value Error if email is not valid
        except ValidationError:
            raise ValueError(_('You must provide a valid email address'))

    #Create User Account and pass in the fields
    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        #Create and save a user with the email password combination
        if not username:
            raise ValueError(_('Users must submit a username'))

        if not first_name:
            raise ValueError(_('Users must submit a first name'))

        if not last_name:
            raise ValueError(_('Users must submit a last name'))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Base User Account: An email address is required'))

        #User Model
        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            **extra_fields
        )

        #Set Password
        user.set_password(password)
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    #Creating a Super User account
    #Create and save a user with the email password combination
    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is__superuser=True"))

        if not password:
            raise ValueError(_("Superusers must have a password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User Account: An email address is required"))

        #SuperUser Model
        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            **extra_fields
        )
        #Set Password
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user
