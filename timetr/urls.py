from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path(r"", TemplateView.as_view(template_name="timetr.html")),
]
