from rest_framework import serializers
from users.models import Users, Dept


class DeptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dept
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    dept = DeptSerializer()

    class Meta:
        model = Users
        fields = ('id', 'url', 'username', 'password', 'user_name', 'dept', 'user_remark')
