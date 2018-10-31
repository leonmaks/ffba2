from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers

from . import views as v


router = routers.DefaultRouter()
router.register(r"users", v.UserViewSet)
router.register("groups", v.GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r"", include(router.urls)),
    path(r"api-auth", include('rest_framework.urls', namespace='rest_framework'))
]
