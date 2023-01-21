from django.db import models
from django.urls import reverse


class Map(models.Model):
    map = models.JSONField(verbose_name='JSON карти')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата останньої зміни')

    def __str__(self):
        return str(self.updated_at)

    def get_absolute_url(self):
        return reverse('map')

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карти'
