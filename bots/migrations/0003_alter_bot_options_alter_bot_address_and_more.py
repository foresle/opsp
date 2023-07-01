# Generated by Django 4.1.4 on 2023-05-21 11:49

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0002_alter_bot_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bot',
            options={'verbose_name': 'Бот', 'verbose_name_plural': 'Боти'},
        ),
        migrations.AlterField(
            model_name='bot',
            name='address',
            field=models.CharField(max_length=120, verbose_name='Адреса'),
        ),
        migrations.AlterField(
            model_name='bot',
            name='description',
            field=markdownx.models.MarkdownxField(verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='bot',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='bot',
            name='support_encryption',
            field=models.BooleanField(verbose_name='Підтримка шифрованих кімнат'),
        ),
    ]
