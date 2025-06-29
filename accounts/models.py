# Imports the base classes needed to create a custom user model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models #Standard Django models module — used to create database models (tables).
from django.utils import timezone #used for fields like date_joined.

#Custom manager to control how users and superusers are created. In Django, managers handle database operations.

class CustomUserManager(BaseUserManager):
    # create_user model
    #Defines how to create a regular user.
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)  #Cleans the email (e.g., converts to lowercase)
        user = self.model(email=email, **extra_fields) #Creates a new CustomUser instance with email and any extra fields (like first_name or last_name).
        user.set_password(password) #Hashes the password


        user.save(using=self._db) #to save in db
        return user #return newly created user

#create super_user model
# creating admin user / super  user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)  #permission of create_user model

class CustomUser(AbstractBaseUser, PermissionsMixin):
    #AbstractBaseUser for Password chacking
    #PermissionsMixin: Permissions-related fields like is_superuser, groups
    email = models.EmailField(unique=True) #(no duplicate accounts)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)#Allows access to the Django admin panel when True.
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  #Tells Django which field to use for logging in (instead of username).
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email  # It’ll show as the email instead of something like CustomUser object (1).



