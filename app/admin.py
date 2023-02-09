from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name', 'description')
    search_fields = ('name', 'id')
    prepopulated_fields = {"slug" : ("name",)}

admin.site.register(Skill,SkillAdmin)

class InterestsAdmin(admin.ModelAdmin):
    list_display = ("name", 'description')
    list_display_links = ("name",'description')
    search_fields = ("name", 'id')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Interest, InterestsAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_created', 'meta_description', 'get_post_photo', 'published')
    list_display_links = ('title', 'meta_description')
    search_fields = ('title', 'meta_description')
    prepopulated_fields = {"slug" : ("title",)}
    list_editable = ('published','slug')


    def get_post_photo(self, object):
        if object.image_under_title:
            return mark_safe(f"<img src='{object.image_under_title.url}' width=50>")
    
admin.site.register(Post, PostAdmin)
