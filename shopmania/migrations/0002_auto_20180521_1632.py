# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-21 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopmania', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_1',
            field=models.ImageField(blank=True, upload_to='shopmania/static/products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='shopmania/static/products/%Y/%m/%d'),
        ),
    ]