import uuid

from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    slug = models.SlugField(blank=True,null=True)
    description = models.CharField(null=True, blank=True, max_length=255)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Interest(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    slug = models.SlugField(blank=True,null=True)
    description = models.CharField(max_length=255,blank=True,null=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Interests'
        verbose_name_plural = 'Interests'

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

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'