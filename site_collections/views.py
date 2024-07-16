from django.shortcuts import render

from django.template.loader import get_template
from .forms import chat_form
from .models import collection,collection_target


def index(request):
    collection_target_list = collection_target.objects.all()
    context = {
        "collection_target_list":collection_target_list
    }
    return render(request,"site_collections/index.html",context)
def collections(request,collection_target_name):
    target = collection_target.objects.get(name=collection_target_name)
    collection_list = target.collection_set.all()
    context = {
        "collection_list":collection_list,
        "collection_target_list":collection_target.objects.order_by("time_created")[:5]
    }
    return render(request, "site_collections/collections.html", context)
def chat(request):
    if request.method == "POST":
        form = chat_form(request.POST)

        if form.is_valid():
            message = form.cleaned_data["question"]
            #make api call here
            context = {
                "response":"response"
            }
            render(request,"site_collections/chat.html",context)

    else:
        form = chat_form()
    return render(request, "site_collections/chat.html",{"form": form})
def manage_collections(request):
    '''
    if request.method == "POST":
        form = collection_target_form(request.POST)

        if form.is_valid():


    else:
        form = chat_form()
    '''
    return render(request, "site_collections/collection_manager.html")
