from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()

router.register('auth/', TokenObtainPairView.as_view())
router.register('auth/refresh/', TokenRefreshView.as_view())