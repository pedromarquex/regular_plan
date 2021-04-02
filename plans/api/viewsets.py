from rest_framework.viewsets import ModelViewSet
from plans.models import Plan

from .serializers import PlanSerializer


class RegularPlanViewSet(ModelViewSet):
    serializer_class = PlanSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return Plan.objects.filter(publish=True)
