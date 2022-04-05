from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group

admin.site.site_header = "Teaching Admin Panel"
admin.site.site_title = "Teaching API"
admin.site.index_title = "Teaching API"

admin.site.unregister(Group)# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'password', 'position',)
    list_display_links = ('id', 'first_name', 'last_name')

@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image',)
    list_display_links = ('id', 'title',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'job',)
    list_display_links = ('id', 'title',)

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'yt_video', 'lesson_status', 'sections', 'files')
    list_display_links = ('id', 'title', 'link', 'yt_video', 'lesson_status', 'sections', 'files')