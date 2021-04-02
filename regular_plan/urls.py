from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from core.urls import router as core_router
from plans.urls import router as plans_router

urlpatterns = [
    path('', include(core_router.urls)),
    path('plans/', include(plans_router.urls)),
    path('admin/', admin.site.urls),
]
