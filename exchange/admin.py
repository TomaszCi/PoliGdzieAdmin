from django.contrib import admin
from db.settings import DB_VERSION
# from exchange.models import building
# 

from exchange.models import *

class BuildingAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        admin.ModelAdmin.save_model(self, request, obj, form, change)
        version = Version.objects.first()
        if not version:
            Version.objects.create(value=1)
        else:
            version.incVal()
            version.save()
        
admin.site.register(Building, BuildingAdmin)

class UnitAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        admin.ModelAdmin.save_model(self, request, obj, form, change)
        version = Version.objects.first()
        if not version:
            Version.objects.create(value=1)
        else:
            version.incVal()
            version.save()

admin.site.register(Unit, UnitAdmin)

class RoomAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        admin.ModelAdmin.save_model(self, request, obj, form, change)
        version = Version.objects.first()
        if not version:
            Version.objects.create(value=1)
        else:
            version.incVal()
            version.save()

admin.site.register(Room, RoomAdmin)


class NavigationpointAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        admin.ModelAdmin.save_model(self, request, obj, form, change)
        version = Version.objects.first()
        if not version:
            Version.objects.create(value=1)
        else:
            version.incVal()
            version.save()

admin.site.register(Navigationpoint, NavigationpointAdmin)

class NavigationconnectionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        admin.ModelAdmin.save_model(self, request, obj, form, change)
        version = Version.objects.first()
        if not version:
            Version.objects.create(value=1)
        else:
            version.incVal()
            version.save()

admin.site.register(Navigationconnection, NavigationconnectionAdmin)

class SpecialconnectionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        admin.ModelAdmin.save_model(self, request, obj, form, change)
        version = Version.objects.first()
        if not version:
            Version.objects.create(value=1)
        else:
            version.incVal()
            version.save()
        
admin.site.register(Specialconnection, SpecialconnectionAdmin)

class BuildingentryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        admin.ModelAdmin.save_model(self, request, obj, form, change)
        version = Version.objects.first()
        if not version:
            Version.objects.create(value=1)
        else:
            version.incVal()
            version.save()
        
admin.site.register(Buildingentry, BuildingentryAdmin)