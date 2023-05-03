from django.contrib import admin
from .models import MenuItem, Menu


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    # fields = ['name', ]
    list_display = ['name']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
