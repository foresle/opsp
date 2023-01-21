from django.db import models
from django.urls import reverse


class Tip(models.Model):
    category = models.CharField(choices=(('matrix', 'matrix'), ('mumble', 'mumble')), max_length=6,
                                verbose_name='Категорія')
    text = models.TextField(max_length=450, verbose_name='Текст')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('tip_detail', args=(self.pk,))

    class Meta:
        verbose_name = 'Підказка'
        verbose_name_plural = 'Підказки'
