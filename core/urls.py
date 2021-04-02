from rest_framework import routers

from core.api.viewsets import RegularPlanViewSet

router = routers.DefaultRouter()
router.register('', RegularPlanViewSet, basename='RegularPlan')
