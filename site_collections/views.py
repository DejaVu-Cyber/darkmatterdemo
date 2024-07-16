from django.shortcuts import render

from django.template.loader import get_template

from .models import collection,collection_target


def index(request):
    collection_target_list = collection_target.objects.order_by("time_created")[:5]
    context = {
        "collection_target_list":collection_target_list
    }
    return render(request,"site_collections/index.html",context)


