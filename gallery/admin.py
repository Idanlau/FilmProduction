from django.contrib import admin
from .models import movies,behind_the_scene
# Register your models here.


class Gallery(admin.ModelAdmin):
    model = movies
    list_display = ('title',)

class Behind(admin.ModelAdmin):
    model = behind_the_scene
    list_display = ('title',)

admin.site.register(movies,Gallery)
admin.site.register(behind_the_scene,Behind)