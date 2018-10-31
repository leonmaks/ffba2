from django.urls import path
from django.views.generic import TemplateView


app_name = "tt"

urlpatterns = [
    path(r"", TemplateView.as_view(template_name="ttt.html")),
    path(r"tt", TemplateView.as_view(template_name="tt.html")),
]
