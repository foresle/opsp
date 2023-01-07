from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Bot(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    support_encryption = models.BooleanField()
    description = MarkdownxField()

    @property
    def formatted_description(self):
        return markdownify(self.description)

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('bot_detail', args=(self.pk,))
