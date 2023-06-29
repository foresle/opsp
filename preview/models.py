from django.db import models


class Phrases(models.Model):
    phrase = models.CharField(verbose_name='Фраза', max_length=320, unique=True, null=False, blank=False)
    priority = models.IntegerField(verbose_name='Пріоритет', default=0, null=False, blank=False)

    class Meta:
        verbose_name = 'Фраза'
        verbose_name_plural = 'Фрази'

    def __str__(self):
        return self.phrase
