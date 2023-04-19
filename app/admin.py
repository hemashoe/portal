from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Skill, Interest


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'get_profile_photo', 'get_profile_photo')
    list_display_links = ('name', 'description')
    search_fields = ('name', 'id')
    prepopulated_fields = {"slug": ("name",)}

    def get_profile_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    def get_wallpaper_photo(self, object):
        if object.wallpaper:
            return mark_safe(f"<img src='{object.wallpaper.url}' width=50>")


@admin.register(Interest)
class InterestsAdmin(admin.ModelAdmin):
    list_display = ("name", 'description', 'get_profile_photo', 'get_profile_photo')
    list_display_links = ("name", 'description')
    search_fields = ("name", 'id')
    prepopulated_fields = {"slug": ("name",)}

    def get_profile_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    def get_wallpaper_photo(self, object):
        if object.wallpaper:
            return mark_safe(f"<img src='{object.wallpaper.url}' width=50>")
