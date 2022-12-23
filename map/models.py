from django.db import models
from django.urls import reverse


class Map(models.Model):
    map = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.updated_at)

    def get_absolute_url(self):
        return reverse('map')
