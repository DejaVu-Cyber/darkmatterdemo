from django.urls import path, re_path, include
from site_collections.views import index

urlpatterns = [
    re_path(r"^index/", index, name="index"),
]