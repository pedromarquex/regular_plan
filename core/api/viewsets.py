from rest_framework.viewsets import ModelViewSet
from core.models import MyUser

from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['post']
    queryset = MyUser.objects.all()
