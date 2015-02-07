from os.path import os
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.http import JsonResponse

from db.settings import DATABASES
from exchange.models import Version


def index(request):
    version = Version.objects.first()
    if not version:
        version = Version.objects.create(value=1)
    return JsonResponse({'dbVersion': str(version)})

def download(request):
    path = DATABASES['default']['NAME']
    wrapper = FileWrapper(open(path, 'rb'))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(path)
    response['Content-Disposition'] = 'attachment; filename=poligdzie.db'
    return response