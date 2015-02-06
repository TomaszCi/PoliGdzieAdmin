# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('coordX', models.FloatField()),
                ('coordY', models.FloatField()),
                ('address', models.CharField(max_length=200)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('aliases', models.CharField(max_length=200)),
                ('imageResource', models.CharField(max_length=200)),
                ('markerImageResource', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
