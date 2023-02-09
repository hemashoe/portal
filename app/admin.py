from django.contrib import admin
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