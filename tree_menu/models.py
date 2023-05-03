from django.db import models


class MenuItem(models.Model):
    name = models.CharField('name', max_length=255)
    url = models.CharField('url', max_length=255, unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey(
        'Menu',
        on_delete=models.CASCADE,
        related_name='item'
    )

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField('name', max_length=255)

    def __str__(self):
        return self.name

