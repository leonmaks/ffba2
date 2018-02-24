from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginRequiredMixin, View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
