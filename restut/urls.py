from django.urls import path, include
from rest_framework import routers

from . import views as v


app_name = "restut"


router = routers.DefaultRouter()
router.register("users", v.UserViewSet)
router.register("groups", v.GroupViewSet)
router.register("permissions", v.PermissionViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
