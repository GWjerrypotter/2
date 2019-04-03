import django_filters
from worked.models import Gzzj


class GzzjFilter(django_filters.rest_framework.FilterSet):
    user = django_filters.CharFilter(field_name='user__user_name', lookup_expr='contains')
    dept = django_filters.CharFilter(field_name='user__dept__dept', lookup_expr='contains')
    time = django_filters.DateTimeFromToRangeFilter()
    gzzj = django_filters.CharFilter(field_name='gzzj', lookup_expr='contains')

    class Meta:
        model = Gzzj
        fields = "__all__"
