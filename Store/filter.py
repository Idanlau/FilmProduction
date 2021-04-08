import django_filters
from Store.models import products


class StoreFilter(django_filters.FilterSet):
    class Meta:
        model = products
        fields = ['title',]