from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from plans.models import Plan
from core.models import MyUser
from .serializers import PlanSerializer
from ..tasks import send_mail_task


class PlanViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PlanSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return Plan.objects.filter(publish=True)

    @action(detail=True, methods=['get'])
    def subscribe(self, request, pk):
        user = MyUser.objects.get(user=request.user)
        plan = Plan.objects.get(pk=pk)
        user.plans.add(plan)
        return Response(status=status.HTTP_200_OK)


class MyPlanViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PlanSerializer
    http_method_names = ['get', 'post', 'patch']

    def get_queryset(self):
        return Plan.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        request.data['owner'] = request.user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        if request.data['publish']:
            send_mail_task.delay()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
