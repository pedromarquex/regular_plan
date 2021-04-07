from rest_framework import routers

from .api.viewsets import PlanViewSet, MyPlanViewSet

plans_router = routers.DefaultRouter()
plans_router.register('', PlanViewSet, basename='Plan')

my_plans_router = routers.DefaultRouter()
my_plans_router.register('', MyPlanViewSet, basename='MyPlan')
