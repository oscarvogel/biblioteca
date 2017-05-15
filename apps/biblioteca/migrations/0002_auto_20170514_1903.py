# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='libro',
            options={'verbose_name_plural': 'Libros'},
        ),
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='libro'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='detalle',
            field=models.TextField(blank=True),
        ),
    ]
