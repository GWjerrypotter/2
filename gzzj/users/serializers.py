from rest_framework import serializers
from users.models import Users, Dept
from django.contrib.auth.hashers import make_password, check_password


class DeptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dept
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    dept = DeptSerializer()

    class Meta:
        model = Users
        fields = ('id', 'url', 'username', 'password', 'user_name', 'dept', 'is_manager', 'user_remark')


class UserAddSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super(UserAddSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = Users
        fields = ('id', 'url', 'username', 'password', 'user_name', 'dept', 'is_manager', 'user_remark')


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('id', 'username', 'user_name', 'is_manager', 'user_remark')


class UserPasswordSerializer(serializers.ModelSerializer):
    oldpassword = serializers.CharField(write_only=True, help_text="原密码", label="原密码", )
    newpassword = serializers.CharField(write_only=True, help_text="新密码", label="新密码", )

    def update(self, instance, validated_data):
        if check_password(validated_data['oldpassword'], instance.password):
            instance.password = make_password(validated_data['newpassword'])
            instance.is_first_login = False  # 是否首次登录改为否
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("原密码错误")

    class Meta:
        model = Users
        fields = ('oldpassword', 'newpassword')
