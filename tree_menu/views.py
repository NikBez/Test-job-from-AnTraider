from django.shortcuts import render, get_object_or_404

from .assets import get_items
from .models import MenuItem


def main_view(request):
    return render(request, 'base.html')


def menu_items_view(request, path):

    active_item = None
    menu_items = []

    if not path:
        menu_items = MenuItem.objects.filter(parent=None)
        page_title = 'Main page'
    else:
        active_item = get_object_or_404(MenuItem, url=path)
        page_title = active_item.name

    parents, childs = get_items(active_item)


    context = {
        'items': menu_items,
        'parents': parents,
        'childs': childs,
        'active_item': active_item,
        'title': page_title,
        'path': path,
    }
    return render(request, 'menu_pages.html', context=context)