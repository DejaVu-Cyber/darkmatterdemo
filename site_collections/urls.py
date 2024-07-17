from django.urls import path, re_path, include
from site_collections.views import *

urlpatterns = [
    path("index/<str:collection_target_name>/", collections, name = "detail"),
    re_path(r"^index/", index, name="index"),
    path("", chat, name = "chat"),
    path("manage_collections/<str:collection_target_name>/",manage_collections, name = "edit_collection" ),
    path("manage_collections/<str:collection_target_name>/delete", delete_collection, name = "delete_collection"),
    path("manage_collections/",manage_collections, name = "manage_collections" )

]