from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class CBV_example(View):
    template_name = "template.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
