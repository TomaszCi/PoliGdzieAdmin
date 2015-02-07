# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AndroidMetadata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locale', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'android_metadata',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField()),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=75)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExchangeBuilding',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('coordx', models.FloatField(db_column='coordX')),
                ('coordy', models.FloatField(db_column='coordY')),
                ('address', models.CharField(max_length=200)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('aliases', models.CharField(max_length=200)),
                ('imageresource', models.CharField(max_length=200, db_column='imageResource')),
                ('markerimageresource', models.CharField(max_length=200, db_column='markerImageResource')),
            ],
            options={
                'db_table': 'exchange_building',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('name', models.TextField(blank=True)),
                ('address', models.TextField(blank=True)),
                ('coordx', models.TextField(db_column='coordX', blank=True)),
                ('coordy', models.TextField(db_column='coordY', blank=True)),
                ('width', models.IntegerField(null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('aliases', models.TextField(blank=True)),
                ('imageresource', models.TextField(db_column='imageResource', blank=True)),
                ('markerimageresource', models.TextField(db_column='markerImageResource', blank=True)),
                ('imageofbuilding', models.TextField(blank=True)),
                ('descriptionofbuilding', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'building',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Buildingentry',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('coordx', models.FloatField(null=True, db_column='coordX', blank=True)),
                ('coordy', models.FloatField(null=True, db_column='coordY', blank=True)),
                ('building_id', models.IntegerField(null=True, blank=True)),
                ('point_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'buildingEntry',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('name', models.TextField(blank=True)),
                ('building_id', models.IntegerField(null=True, blank=True)),
                ('number', models.IntegerField(null=True, blank=True)),
                ('width', models.IntegerField(null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('drawableid', models.TextField(db_column='drawableId', blank=True)),
                ('tag', models.TextField(blank=True)),
                ('pixelspermeter', models.IntegerField(null=True, db_column='pixelsPerMeter', blank=True)),
            ],
            options={
                'db_table': 'floor',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Navigationconnection',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('navigationpointfirst_id', models.IntegerField(null=True, db_column='navigationPointFirst_id', blank=True)),
                ('navigationpointlast_id', models.IntegerField(null=True, db_column='navigationPointLast_id', blank=True)),
                ('length', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'navigationConnection',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Navigationpoint',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('coordx', models.IntegerField(null=True, db_column='coordX', blank=True)),
                ('coordy', models.IntegerField(null=True, db_column='coordY', blank=True)),
                ('floor_id', models.IntegerField(null=True, blank=True)),
                ('type', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'navigationPoint',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('number', models.TextField(blank=True)),
                ('name', models.TextField(blank=True)),
                ('function', models.TextField(blank=True)),
                ('floor_id', models.IntegerField(null=True, blank=True)),
                ('coordx', models.IntegerField(null=True, db_column='coordX', blank=True)),
                ('coordy', models.IntegerField(null=True, db_column='coordY', blank=True)),
                ('radius', models.IntegerField(null=True, blank=True)),
                ('doorsx', models.IntegerField(null=True, db_column='doorsX', blank=True)),
                ('doorsy', models.IntegerField(null=True, db_column='doorsY', blank=True)),
                ('navigationpointconnection_id', models.IntegerField(null=True, db_column='navigationPointConnection_id', blank=True)),
                ('aliases', models.TextField(blank=True)),
                ('building_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'room',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Specialconnection',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('specialpointlower_id', models.IntegerField(null=True, db_column='specialPointLower_id', blank=True)),
                ('specialpointupper_id', models.IntegerField(null=True, db_column='specialPointUpper_id', blank=True)),
            ],
            options={
                'db_table': 'specialConnection',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('aliases', models.TextField(blank=True)),
                ('building_id', models.IntegerField(null=True, blank=True)),
                ('www', models.TextField(blank=True)),
                ('name', models.TextField(blank=True)),
                ('room_id', models.IntegerField(null=True, blank=True)),
                ('type', models.TextField(blank=True)),
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
            ],
            options={
                'db_table': 'unit',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
