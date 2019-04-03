#
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import viewsets, filters
# from rest_framework.pagination import PageNumberPagination
#
# from users.filter import UsersFilter
# from users.models import Users
# from users.serializers import UserSerializer
#
#
# class UserPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     page_query_param = 'p'
#
#
# class UserListPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     page_query_param = 'p'
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer
#     pagination_class = UserPagination
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     filter_class = UsersFilter
#     search_fields = ('username', 'user_name', 'dept__dept')

