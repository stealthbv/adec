# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20151112_1443'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='Professional',
        ),
    ]
