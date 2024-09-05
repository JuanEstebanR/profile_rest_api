from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """
        Create a new user Profile
        :param email:
        :param name:
        :param password:
        :return:
        """
        if not email:
            raise ValueError('User needs to provide an email address')
        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Create and save a new superuser
        :param email:
        :param name:
        :param password:
        :return:
        """
        user = self.create_user(email, name=name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# Create your models here.
class UserProfile(AbstractUser, PermissionsMixin):
    """
        Database models for users in the system
    """
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    username = None
    class Meta:
        constraints = [models.UniqueConstraint(fields=['email'], name='unique_email')]

    def get_full_name(self):
        """
        Retrieve full name of user
        :return:
        """
        return self.name

    def get_short_name(self):
        """
        Retrieve short name for users
        :return:
        """
        return self.name

    def __str__(self):
        return self.email


class UserFeed(models.Model):
    """
        Model for users Feed
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feeds')
    status_text = models.TextField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f'Feed: {self.status_text}'