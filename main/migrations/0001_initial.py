# Generated by Django 4.2 on 2023-04-17 06:31

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('fullname', models.CharField(max_length=255)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_img', models.ImageField(blank=True, default='defaults/1.png', null=True, upload_to='profiles/')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('interests', models.ManyToManyField(blank=True, to='app.interest')),
                ('skills', models.ManyToManyField(blank=True, to='app.skill')),
            ],
            options={
                'verbose_name': 'Pofile',
                'verbose_name_plural': 'Profiles',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('source_link', models.CharField(max_length=255, unique=True)),
                ('source_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='post/')),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
                ('interests', models.ManyToManyField(blank=True, to='app.interest')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-date_published'],
            },
        ),
    ]
