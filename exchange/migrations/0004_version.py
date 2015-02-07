# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0003_auto_20150207_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
