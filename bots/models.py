from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Bot(models.Model):
    name = models.CharField(max_length=120, verbose_name='Назва')
    address = models.CharField(max_length=120, verbose_name='Адреса')
    support_encryption = models.BooleanField(verbose_name='Підтримка шифрованих кімнат')
    description = MarkdownxField(verbose_name='Опис')

    @property
    def formatted_description(self):
        return markdownify(self.description)

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('bot_detail', args=(self.pk,))

    class Meta:
        verbose_name = 'Бот'
        verbose_name_plural = 'Боти'
