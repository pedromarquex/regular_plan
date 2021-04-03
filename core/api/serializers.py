from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from core.models import MyUser


class DefaultUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class UserSerializer(ModelSerializer):
    user = DefaultUserSerializer()

    class Meta:
        model = MyUser
        fields = ['id', 'name', 'user', 'plans']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        final_user = MyUser.objects.create(**validated_data, user=user)
        return final_user
