from django.shortcuts import render


def menu_items_view(request, path):
    return render(request, 'menu_pages.html')

