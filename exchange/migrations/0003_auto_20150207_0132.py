# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_auto_20150207_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='descriptionofbuilding',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='imageofbuilding',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
