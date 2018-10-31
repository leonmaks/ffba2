from django.contrib import admin
from django.conf import settings
from django.urls import include, path, reverse_lazy
from django.contrib.auth import views as auth_v
from django.views.generic import TemplateView

from . import views as v

urlpatterns = [
    path(r"admin/", admin.site.urls),
    # path(r"org/", include("org.urls")),
    # path(r"todo/", include("todo.urls")),
    # path(r"prod/", include("prod.urls")),
    path(r"sales/", include("sales.urls")),
    # path(r"ae/", include("ae.urls")),
    # path(r"restut/", include("restut.urls")),
    # path(r"novelty/", include("novelty.urls")),      # TODO - delete, temporary app
    # path(r"ponynote/", include("ponynote.urls")),    # TODO - delete, temporary app
    # path(r"timetr/", include("timetr.urls")),    # TODO - delete, temporary app
    # path(r"tt/", include("tt.urls")),    # TODO - delete, temporary app
    path(r"login/", auth_v.LoginView.as_view(), name="login"),
    path(r"logout/", auth_v.LogoutView.as_view(), {'next_page': reverse_lazy("home")}, name="logout"),
    path(r"password-change/?", auth_v.PasswordChangeView.as_view(), name="password-change"),
    path(r"password-change-done/?", auth_v.PasswordChangeDoneView.as_view(), name="password-change-done"),
    path(r"about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path(r"", TemplateView.as_view(template_name="home.html"), {'template_name': "home.html"}, name="home"),
    # path(r"api-auth/", include('rest_framework.urls'))
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r"__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
