from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests, webbrowser
from .forms import chat_form, collection_target_form
from .models import collection,collection_target
from .filters import collection_target_filter
@login_required()
def index(request):
    collection_target_list = collection_target.objects.order_by("-last_modified")

    context = {
        "collection_target_list":collection_target_list
    }
    return render(request,"site_collections/index.html",context)
@login_required()
def collections(request,collection_target_name):
    target = collection_target.objects.get(name=collection_target_name)
    collection_list = target.collection_set.all()

    context = {
        "collection_list":collection_list,
        "collection_target_list":collection_target.objects.order_by("-last_modified"),
    }
    return render(request, "site_collections/collections.html", context)
@login_required()
def chat(request):
    if request.method == "POST":
        form = chat_form(request.POST)

        if form.is_valid():
            message = form.cleaned_data["question"]
            #make api call here
            context = {
                "response":message,
                "form":chat_form()
            }
            return render(request,"site_collections/chat.html",context)

    else:
        form = chat_form()
    return render(request, "site_collections/chat.html",{"form": form})
@login_required()
def manage_collections(request, collection_target_name=None):
    if request.method == "POST" and collection_target_name is not None:
        form = collection_target_form(request.POST,instance=collection_target.objects.get(name=collection_target_name))
    elif request.method == "POST":
        form = collection_target_form(request.POST)
    elif request.method == "GET" and collection_target_name is not None:
        form = collection_target_form(instance=collection_target.objects.get(name=collection_target_name))
        return render(request, "site_collections/collection_manager.html", {"form": form})
    elif request.method =="GET":
        form = collection_target_form()
        return render(request, "site_collections/collection_manager.html", {"form": form})

    if form.is_valid():
        new_collection_target = form.save()
        return render(request, "site_collections/collection_manager.html", {"form":collection_target_form})
    else:
        return render(request, "site_collections/collection_manager.html", {"form": collection_target_form, "errors":form.errors})




@login_required()
def delete_collection(request, collection_target_name):
    target = collection_target.objects.get(name=collection_target_name)
    target.delete()
    collection_target_list = collection_target.objects.all()
    context = {
        "collection_target_list": collection_target_list
    }
    return render(request, "site_collections/index.html", context)
def search_collection_targets(request):
    f = collection_target_filter(request.GET, queryset=collection_target.objects.all())
    return render(request, 'site_collections/search.html', {"filter": f})

def record_collection(request, collection_target_name):
    target = collection_target.objects.get(name=collection_target_name)
    r = requests.get(f'http://localhost:8080/collections_archive/record/{target.host_url}')
    c = collection(translated_url = "x.com", original_url = target.host_url, collection_point = "",target=target)
    c.save()
    return render(request,'site_collections/index.html',{'collection_target_list':collection_target.objects.all()})

def replay_collection(request,collection_target_name, collection_pk):
    target = collection_target.objects.get(name=collection_target_name)
    collection_list = target.collection_set.all()

    context = {
        "collection_list": collection_list,
        "collection_target_list": collection_target.objects.order_by("-last_modified"),
        "collection":collection.objects.get(pk=collection_pk)
    }
    return render(request,'site_collections/replay.html',context)