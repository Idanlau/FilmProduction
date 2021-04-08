from django.contrib import admin
from .models import products



class productAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(products,productAdmin)