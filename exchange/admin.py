from django.contrib import admin
# from exchange.models import building
# 

from exchange.models import *

admin.site.register(Building)
admin.site.register(Unit)
admin.site.register(Room)
admin.site.register(Navigationpoint)
admin.site.register(Navigationconnection)
admin.site.register(Specialconnection)
admin.site.register(Buildingentry)