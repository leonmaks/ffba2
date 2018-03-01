from django.contrib import admin
from django.conf import settings
from django.urls import include, path, reverse_lazy
from django.contrib.auth import views as auth_v
from django.views.generic import TemplateView

from . import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path("prod/", include("prod.urls")),
    path("ae/", include("ae.urls")),
    path("rpt/", include("rpt.urls")),
    path(r"login/", auth_v.login, name="login"),
    path(r"logout/", auth_v.logout, {'next_page': reverse_lazy("home")}, name="logout"),
    path(r"password-change/?", auth_v.password_change, name="password-change"),
    path(r"password-change-done/?", auth_v.password_change_done, name="password-change-done"),
    path(r"about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path(r"home/", v.Home.as_view(), {'template_name': "home.html"}, name="home"),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r"__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
