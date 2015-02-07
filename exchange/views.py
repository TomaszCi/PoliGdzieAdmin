from django.http import HttpResponse
from django.http import JsonResponse
from exchange.models import Version
from db.settings import DATABASES

def index(request):
    version = Version.objects.first()
    if not version:
        version = Version.objects.create(value=1)
    return JsonResponse({'dbVersion': str(version)})

def download(request):
    response = HttpResponse(DATABASES['name'])
    return response