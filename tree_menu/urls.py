from django.urls import re_path
from .views import menu_items_view


urlpatterns = [
    re_path(r'^(?P<path>.*)$', menu_items_view, name='menu_items_page'),
]