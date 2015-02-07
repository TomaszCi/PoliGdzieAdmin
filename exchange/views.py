from django.http import HttpResponse
from db.settings import DB_VERSION
from exchange.models import Version

def index(request):
    version = Version.objects.first()
    if not version:
        version = Version.objects.create(value=1)
    
    
    return HttpResponse("{\n\t\"dbVersion\" : " + str(version) + "\n}")