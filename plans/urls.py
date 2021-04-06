from rest_framework import routers

from .api.viewsets import PlanViewSet

router = routers.DefaultRouter()
router.register('', PlanViewSet, basename='Plan')
