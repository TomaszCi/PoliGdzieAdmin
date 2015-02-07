from django.conf.urls import patterns, include, url
from django.contrib import admin
from exchange.views import *
import exchange

urlpatterns = patterns('',
    url(r'^version/', exchange.views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^download/', exchange.views.download),
)