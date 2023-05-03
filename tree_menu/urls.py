from django.urls import path, re_path
from .views import menu_items_view


urlpatterns = [
    # path('', main_view, name='main_view'),
    re_path(r'^(?P<path>.*)$', menu_items_view, name='menu_items_page'),
]

