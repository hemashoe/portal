from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'fullname', 'is_active', 'is_staff', 'created_at')
    list_display_links = ('username', 'fullname')
    list_editable = ("is_active", 'is_staff')
    search_fields = ('username', 'fullname')
    
admin.site.register(User, UserAdmin)
