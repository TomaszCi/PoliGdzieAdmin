# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AndroidMetadata(models.Model):
    locale = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'android_metadata'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Building(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    name = models.TextField(blank=True)  # This field type is a guess.
    address = models.TextField(blank=True)  # This field type is a guess.
    coordx = models.TextField(db_column='coordX', blank=True)  # Field name made lowercase. This field type is a guess.
    coordy = models.TextField(db_column='coordY', blank=True)  # Field name made lowercase. This field type is a guess.
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    aliases = models.TextField(blank=True)  # This field type is a guess.
    imageresource = models.TextField(db_column='imageResource', blank=True)  # Field name made lowercase. This field type is a guess.
    markerimageresource = models.TextField(db_column='markerImageResource', blank=True)  # Field name made lowercase. This field type is a guess.
    imageofbuilding = models.TextField(blank=True)
    descriptionofbuilding = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'building'


class Buildingentry(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    coordx = models.FloatField(db_column='coordX', blank=True, null=True)  # Field name made lowercase.
    coordy = models.FloatField(db_column='coordY', blank=True, null=True)  # Field name made lowercase.
    building_id = models.IntegerField(blank=True, null=True)
    point_id = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return "Wejscie numer " + str(self.id) + " do budynku numer " + str(self.building_id)

    class Meta:
        managed = True
        db_table = 'buildingEntry'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExchangeBuilding(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=200)
    coordx = models.FloatField(db_column='coordX')  # Field name made lowercase.
    coordy = models.FloatField(db_column='coordY')  # Field name made lowercase.
    address = models.CharField(max_length=200)
    width = models.IntegerField()
    height = models.IntegerField()
    aliases = models.CharField(max_length=200)
    imageresource = models.CharField(db_column='imageResource', max_length=200)  # Field name made lowercase.
    markerimageresource = models.CharField(db_column='markerImageResource', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exchange_building'


class Floor(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    name = models.TextField(blank=True)  # This field type is a guess.
    building_id = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    drawableid = models.TextField(db_column='drawableId', blank=True)  # Field name made lowercase. This field type is a guess.
    tag = models.TextField(blank=True)  # This field type is a guess.
    pixelspermeter = models.IntegerField(db_column='pixelsPerMeter', blank=True, null=True)  # Field name made lowercase.
    
    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'floor'


class Navigationconnection(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    navigationpointfirst_id = models.IntegerField(db_column='navigationPointFirst_id', blank=True, null=True)  # Field name made lowercase.
    navigationpointlast_id = models.IntegerField(db_column='navigationPointLast_id', blank=True, null=True)  # Field name made lowercase.
    length = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "Polaczenie miedzy " + str(self.navigationpointfirst_id) + " a " + str(self.navigationpointlast_id)
    
    class Meta:
        managed = True
        db_table = 'navigationConnection'


class Navigationpoint(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    coordx = models.IntegerField(db_column='coordX', blank=True, null=True)  # Field name made lowercase.
    coordy = models.IntegerField(db_column='coordY', blank=True, null=True)  # Field name made lowercase.
    floor_id = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True)  # This field type is a guess.

    def __unicode__(self):
        return "Punkt nawigacyjny numer " + str(self.id) + " na pietrze numer " + str(self.floor_id)
    
    class Meta:
        managed = True
        db_table = 'navigationPoint'


class Room(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    number = models.TextField(blank=True)  # This field type is a guess.
    name = models.TextField(blank=True)  # This field type is a guess.
    function = models.TextField(blank=True)  # This field type is a guess.
    floor_id = models.IntegerField(blank=True, null=True)
    coordx = models.IntegerField(db_column='coordX', blank=True, null=True)  # Field name made lowercase.
    coordy = models.IntegerField(db_column='coordY', blank=True, null=True)  # Field name made lowercase.
    radius = models.IntegerField(blank=True, null=True)
    doorsx = models.IntegerField(db_column='doorsX', blank=True, null=True)  # Field name made lowercase.
    doorsy = models.IntegerField(db_column='doorsY', blank=True, null=True)  # Field name made lowercase.
    navigationpointconnection_id = models.IntegerField(db_column='navigationPointConnection_id', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(blank=True)  # This field type is a guess.
    building_id = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name + " w budynku numer " + str(self.building_id)
    
    class Meta:
        managed = True
        db_table = 'room'


class Specialconnection(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    specialpointlower_id = models.IntegerField(db_column='specialPointLower_id', blank=True, null=True)  # Field name made lowercase.
    specialpointupper_id = models.IntegerField(db_column='specialPointUpper_id', blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return "Polaczenie specjalne miedzy " + str(self.specialpointlower_id) + " a " + str(self.specialpointupper_id)
    
    class Meta:
        managed = True
        db_table = 'specialConnection'


class Unit(models.Model):
    aliases = models.TextField(blank=True)  # This field type is a guess.
    building_id = models.IntegerField(blank=True, null=True)
    www = models.TextField(blank=True)  # This field type is a guess.
    name = models.TextField(blank=True)  # This field type is a guess.
    room_id = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True)  # This field type is a guess.
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?


    def __unicode__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'unit'


class Version(models.Model):
    value = models.IntegerField()
    
    def __unicode__(self):
        return str(self.value)
    
    def incVal(self):
        self.value += 1
        