from django.urls import path


def main_view():
    pass

urlpatterns = [
    path('', main_view, name='main_view'),
]

