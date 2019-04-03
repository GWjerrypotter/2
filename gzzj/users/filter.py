import django_filters
from users.models import Users


class UsersFilter(django_filters.rest_framework.FilterSet):
    dept = django_filters.CharFilter(field_name='dept__dept', lookup_expr='contains')

    class Meta:
        model = Users
        fields = '__all__'
