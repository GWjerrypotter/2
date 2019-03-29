import django_filters
from users.models import Users
from worked.models import Gzzj


class UsersFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Users
        fields = ['username', 'user_name']


class GzzjFilter(django_filters.rest_framework.FilterSet):
    user = django_filters.CharFilter(field_name='user__user_name', lookup_expr='contains')
    time = django_filters.DateTimeFromToRangeFilter()
    gzzj = django_filters.CharFilter(field_name='gzzj', lookup_expr='contains')

    class Meta:
        model = Gzzj
        fields = "__all__"
