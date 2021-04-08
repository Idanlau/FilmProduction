from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileName(admin.ModelAdmin):
    model = Profile
    list_display = ('user',)

admin.site.register(Profile,ProfileName)
# Register your models here.
