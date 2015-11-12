# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adec', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='timestamp',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='facebook_ID',
            new_name='facebook',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='instgram_ID',
            new_name='instagram',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='updated',
            new_name='modified',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Profession',
            new_name='profession',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='twitter_ID',
            new_name='twitter',
        ),
    ]
