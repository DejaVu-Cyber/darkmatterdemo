
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import collection, collection_target

admin.site.register(collection)
admin.site.register(collection_target)

# Register your models here.
