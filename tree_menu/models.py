from django.db import models

class MenuItem(models.Model):
    name = models.CharField('name', max_length=50)
    url = models.CharField('url', max_length=100)
    parent = models.ForeignKey('MenuItem', on_delete=models.CASCADE, related_name='childes')


