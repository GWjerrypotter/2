
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from users.filter import UsersFilter
from users.models import Users
from users.serializers import UserSerializer, UserAddSerializer, UserUpdateSerializer, UserPasswordSerializer
from worked.filter import GzzjFilter
from worked.models import Gzzj
from worked.serializers import GzzjSerializer, GzzjlistSerializer, GzzjUpdateSerializer


class GzzjPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'


class GzzjListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'


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


class GzzjUpdateViewSet(viewsets.ModelViewSet):
    queryset = Gzzj.objects.all()
    permission_classes = (IsAuthenticated, BasePermission)  # 必须是登陆用户
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)  # JWT认证
    serializer_class = GzzjUpdateSerializer
    pagination_class = GzzjPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GzzjFilter


class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'


class UserListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = (IsAuthenticated, BasePermission)  # 必须是登陆用户
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)  # JWT认证
    serializer_class = UserSerializer
    pagination_class = UserPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UsersFilter
    search_fields = ('username', 'user_name', 'dept__dept')


class UserAddViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = (IsAuthenticated, BasePermission)  # 必须是登陆用户
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)  # JWT认证
    serializer_class = UserAddSerializer
    pagination_class = UserPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UsersFilter
    search_fields = ('username', 'user_name', 'dept__dept')


class UserUpdateViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = (IsAuthenticated, BasePermission)  # 必须是登陆用户
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)  # JWT认证
    serializer_class = UserUpdateSerializer
    pagination_class = UserPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UsersFilter
    search_fields = ('username', 'user_name')


class UserPasswordViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Users.objects.all()
    permission_classes = (IsAuthenticated, BasePermission)  # 必须是登陆用户
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)  # JWT认证
    serializer_class = UserPasswordSerializer
