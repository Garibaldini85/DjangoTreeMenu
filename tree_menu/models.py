from django.db import models
from django.urls import NoReverseMatch, reverse


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, help_text='Путь или name URL')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_absolute_url(self):
        try:
            return reverse(self.url)
        except NoReverseMatch:
            return self.url

    def __str__(self):
        return self.name
