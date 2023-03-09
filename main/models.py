from PIL import Image
import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from app.models import Interest, Skill


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255, null=False)
    bio = models.TextField(blank=True, null=True)
    profile_img = models.ImageField(null=True, blank=True, upload_to='profiles/', default='defaults/1.png')
    created_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    skills = models.ManyToManyField(Skill,blank=True)
    interests = models.ManyToManyField(Interest,blank=True)

    class Meta:
        verbose_name = 'Pofile'
        verbose_name_plural = 'Profiles'
        ordering = ['-created_date']
            
    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse("profile_detail", args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        if self.profile_img:
            img = Image.open(self.profile_img.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_img.path)


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    source_link = models.CharField(max_length=255, unique=True)
    source_id = models.CharField(max_length=255,unique=True, blank=True)
    description = models.TextField()
    body = RichTextUploadingField()
    title_image = models.ImageField(upload_to="post/", null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    interests = models.ManyToManyField(Interest, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-date_published']
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("profile_detail;", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save()

        if self.title_image:
            img = Image.open(self.title_image.path)
            if img.height > 720 or img.width > 480:
                output_size = (720, 480)
                img.thumbnail(output_size)
                img.save(self.title_image.path)


class News(models.Model):
    title = models.CharField(max_length=255,unique=True)
    description = models.TextField()
    body = RichTextUploadingField()
    slug= models.SlugField(max_length=255, unique=True)
    source_link = models.CharField(max_length=255, unique=True)
    source_id = models.CharField(max_length=255,unique=True, blank=True)
    news_image = models.ImageField(upload_to=f"articles/", null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    interests = models.ManyToManyField(Interest, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default='Null', blank=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-date_published']
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("News", args=[str(self.slug)])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        if self.news_image:
            img = Image.open(self.news_image.path)
            if img.height > 720 or img.width > 480:
                output_size = (720, 480)
                img.thumbnail(output_size)
                img.save(self.news_image.path)