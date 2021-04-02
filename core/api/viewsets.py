from rest_framework.viewsets import ModelViewSet
from core.models import RegularPlan

from .serializers import RegularPlanSerializer


class RegularPlanViewSet(ModelViewSet):
    serializer_class = RegularPlanSerializer
    http_method_names = ['get']

    def get_queryset(self):
        return RegularPlan.objects.filter(publish=True)
