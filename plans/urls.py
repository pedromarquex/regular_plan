from rest_framework import routers

from .api.viewsets import RegularPlanViewSet

router = routers.DefaultRouter()
router.register('', RegularPlanViewSet, basename='RegularPlan')