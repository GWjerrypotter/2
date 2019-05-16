import django_filters
from users.models import Users


class UsersFilter(django_filters.rest_framework.FilterSet):
    user_name = django_filters.CharFilter(field_name='user_name', lookup_expr='contains')
    username = django_filters.CharFilter(field_name='username', lookup_expr='contains')
    dept = django_filters.CharFilter(field_name='dept__dept', lookup_expr='contains')

    class Meta:
        model = Users
        fields = ['id', 'user_name', 'username', 'dept', 'is_manager']
