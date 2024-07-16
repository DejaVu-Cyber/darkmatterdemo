from django.urls import path, re_path, include
from site_collections.views import index, collections, chat, manage_collections

urlpatterns = [
    path("index/<str:collection_target_name>/", collections, name = "detail"),
    re_path(r"^index/", index, name="index"),
    path("chat", chat, name = "chat"),
    path("manage_collections",manage_collections, name = "manage_collections" )
]