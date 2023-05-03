from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'parent', 'menu']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name']
