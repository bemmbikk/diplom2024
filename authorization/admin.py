from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','phone_number']
admin.site.register(Profile, ProfileAdmin)