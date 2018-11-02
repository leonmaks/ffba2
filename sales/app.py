from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView


class Sales(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    # TODO: define permissions
    permission_required = ("sales.xxx")

    # template_name = "sales.html"
