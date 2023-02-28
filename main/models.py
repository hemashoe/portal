import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from PIL import Image

from app.models import Interest, Skill

# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255, null=False)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='defaults/1.png')
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

        if self.image:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    source_link = models.CharField(max_length=255, unique=True)
    source_id = models.CharField(max_length=255,unique=True, blank=True)
    description = RichTextUploadingField()
    body = RichTextUploadingField()
    title_image = models.ImageField(upload_to="post/%Y/%M/%d", null=True, blank=True)
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

class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    text = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
  
    def __str__(self):
        return self.text
    

class News(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    title = models.CharField(max_length=255,unique=True)
    description = RichTextUploadingField()
    body = RichTextUploadingField()
    slug= models.SlugField(max_length=255, unique=True)
    source_link = models.CharField(max_length=255, unique=True)
    source_id = models.CharField(max_length=255,unique=True, blank=True)
    news_image = models.ImageField(upload_to="articles/%Y/%M/%d", null=True, blank=True)
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
