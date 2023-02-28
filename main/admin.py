from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.

class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'fullname', 'get_profile_photo', 'status')
    list_display_links = ('user', 'fullname')
    list_editable = ('status', 'email')
    readonly_fields = ('created_date', 'get_profile_photo')
    search_fields = ('user', 'email', 'fullname')
    save_on_top = True

    def get_profile_photo(self, object):
        if object.profile_img:
            return mark_safe(f"<img src='{object.profile_img.url}' width=50>")
    
admin.site.register(Profile, ProfilesAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'source_link', 'date_published', 'get_post_photo', 'published')
    list_display_links = ('title','source_link',)
    search_fields = ('title',)
    prepopulated_fields = {"slug" : ("title",)}
    list_editable = ('published','slug')

    def get_post_photo(self, object):
        if object.title_image:
            return mark_safe(f"<img src='{object.title_image.url}' width=50>")


admin.site.register(Post, PostAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'source_link','date_published', 'get_post_photo', 'published')
    list_display_links = ('title', 'source_link',)
    search_fields = ('title', 'description',)
    prepopulated_fields = {"slug" : ("title",)}
    list_editable = ('published','slug')

    def get_post_photo(self, object):
        if object.news_image:
            return mark_safe(f"<img src='{object.news_image.url}' width=50>")

admin.site.register(News, NewsAdmin)
