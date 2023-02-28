# Generated by Django 4.1.7 on 2023-02-28 09:25

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
                ('image', models.ImageField(blank=True, default='defaults/1.png', null=True, upload_to='profiles/')),
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
                ('source_id', models.CharField(blank=True, max_length=255, unique=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='post/%Y/%M/%d')),
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
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('source_link', models.CharField(max_length=255, unique=True)),
                ('source_id', models.CharField(blank=True, max_length=255, unique=True)),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='articles/%Y/%M/%d')),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=True)),
                ('author', models.ForeignKey(blank=True, default='Null', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.profile')),
                ('interests', models.ManyToManyField(blank=True, to='app.interest')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'ordering': ['-date_published'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.post')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['-created_on'],
            },
        ),
    ]
