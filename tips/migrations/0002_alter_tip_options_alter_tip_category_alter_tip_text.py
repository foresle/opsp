# Generated by Django 4.1.4 on 2023-05-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tip',
            options={'verbose_name': 'Підказка', 'verbose_name_plural': 'Підказки'},
        ),
        migrations.AlterField(
            model_name='tip',
            name='category',
            field=models.CharField(choices=[('matrix', 'matrix'), ('mumble', 'mumble')], max_length=6, verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='tip',
            name='text',
            field=models.TextField(max_length=450, verbose_name='Текст'),
        ),
    ]
