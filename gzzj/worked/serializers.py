from rest_framework import serializers

from users.serializers import UserSerializer
from worked.models import Gzzj


class GzzjSerializer(serializers.ModelSerializer):
    # time = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)

    class Meta:
        model = Gzzj
        fields = ('id', 'url', 'user', 'gzzj', 'time')


class GzzjlistSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Gzzj
        fields = ('id', 'url', 'user', 'gzzj', 'time')


class GzzjUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gzzj
        fields = ('id', 'gzzj', 'time')
