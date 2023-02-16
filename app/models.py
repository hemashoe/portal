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