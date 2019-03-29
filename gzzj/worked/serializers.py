from rest_framework import serializers
from rest_framework.response import Response

from users.models import Users
from worked.models import Gzzj


# class GzzjSerializer(serializers.ModelSerializer):
#     time = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)
#
#     class Meta:
#         model = Gzzj
#         fields = '__all__'
#         read_only_fields = ('password', 'username')
#
#
# class UserSerializer(serializers.ModelSerializer):
#     gzzjs = GzzjSerializer(many=True)
#
#     class Meta:
#         model = Users
#         fields = ('url', 'username', 'password', 'user_name', 'user_remark', 'gzzjs')
#
#     def create(self, validated_data):
#         gzzjs_data = validated_data.pop('gzzj')
#         user_name = Users.objects.create(**validated_data)
#         for gzzj_data in gzzjs_data:
#             Gzzj.objects.create(user=user_name, **gzzj_data)
#         return user_name


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'url', 'username', 'password', 'user_name', 'user_remark')


class GzzjSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)

    class Meta:
        model = Gzzj
        fields = ('id', 'url', 'user', 'gzzj', 'time')


class GzzjlistSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)
    user = UserSerializer()

    class Meta:
        model = Gzzj
        fields = ('id', 'url', 'user', 'gzzj', 'time')