from django.contrib import admin
from .models import UserProfile, UserFeed
# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'is_active', 'is_staff', 'username']
    search_fields = ['email']


@admin.register(UserFeed)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['user', 'status_text', 'created']
