from django_filters import CharFilter, FilterSet, RangeFilter

from house.models import House


class HouseFilter(FilterSet):
    address = CharFilter(lookup_expr='icontains')
    price = RangeFilter(field_name='price')

    class Meta:
        model = House
        fields = '__all__'
        exclude = ['title', 'description', 'owner', 'created', 'last_modified', ]


class HouseSearchFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')
    address = CharFilter(lookup_expr='icontains')
    description = CharFilter(lookup_expr='icontains')

    class Meta:
        model = House
        fields = ['title', 'address', 'description', ]
