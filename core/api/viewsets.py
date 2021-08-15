from rest_framework import mixins
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.models import MyUser

from .serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()

    @authentication_classes([JWTAuthentication])
    def list(self, request, *args, **kwargs):
        return Response()

