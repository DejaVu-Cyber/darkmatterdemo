from .models import *
import requests
def record():
    for target in collection_target.objects.all():
        r = requests.get(f'http"//localhost:8080/collections_archive/record/{target.host_url}')