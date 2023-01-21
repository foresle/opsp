from django.db import models
from django.urls import reverse


class Tip(models.Model):
    category = models.CharField(choices=(('matrix', 'matrix'), ('mumble', 'mumble')), max_length=6)
    text = models.TextField(max_length=450)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('tip_detail', args=(self.pk,))
