
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from users.models import Users
from worked.filter import UsersFilter, GzzjFilter
from worked.models import Gzzj
from worked.serializers import UserSerializer, GzzjSerializer, GzzjlistSerializer


class GzzjPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'


class GzzjListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    pagination_class = GzzjPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UsersFilter
    search_fields = ('username', 'user_name')


class GzzjViewSet(viewsets.ModelViewSet):
    queryset = Gzzj.objects.all()
    serializer_class = GzzjSerializer
    pagination_class = GzzjPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GzzjFilter


class GzzjListViewSet(viewsets.ModelViewSet):
    queryset = Gzzj.objects.all()
    serializer_class = GzzjlistSerializer
    pagination_class = GzzjListPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GzzjFilter

