# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-16 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20151116_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.EmailField(blank=True, max_length=120, null=True),
        ),
    ]
