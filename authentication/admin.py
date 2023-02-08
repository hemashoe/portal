from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

class AllUsers(admin.ModelAdmin):
    list_display = ('username', 'fullname', 'is_active', 'is_staff', 'created_at')
    list_display_links = ('username', 'fullname')
    search_fields = ('username', 'fullname')
    
admin.site.register(User, AllUsers)


class ProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'fullname', 'get_profile_photo', 'status')
    list_display_links = ('user', 'fullname')
    list_editable = ('status', 'email')
    readonly_fields = ('created_date', 'get_profile_photo')
    save_on_top = True

    def get_profile_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")
    
admin.site.register(Profile, ProfilesAdmin)