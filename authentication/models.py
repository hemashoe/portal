from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid

from app.models import *


class Profile(models.Model):
    user = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255, null=False)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='defaults/1.png')
    created_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    skills = models.ManyToManyField(Skill,blank=True)
    interests = models.ManyToManyField(Interest,blank=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Pofile'
        verbose_name_plural = 'Profiles'
        ordering = ['-created_date']

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        user = self.model(username=username)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    fullname = models.CharField(max_length=255,unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD ='username'
    objects= UserManager()

    def __str__(self) -> str:
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255, blank=True)
    meta_description = models.CharField(max_length=155, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField(max_length=100000)
    image_under_title = models.ImageField(upload_to="post/%Y/%M/%d", null=True, blank=True)
    image_in_post = models.ImageField(upload_to='post/%Y/%M/%d', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    interests = models.ManyToManyField(Interest, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default='Null', blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'