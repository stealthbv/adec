# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adec', '0003_auto_20151112_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='professional',
            name='city',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='professional',
            name='country',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
