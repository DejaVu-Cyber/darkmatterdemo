import django_filters
from .models import collection_target

class collection_target_filter(django_filters.FilterSet):
    class Meta:
        model = collection_target
        fields = {
            'name': ['iexact'],
            'last_modified':['range']
        }