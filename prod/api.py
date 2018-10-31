# from django.views.generic import ListView, CreateView, UpdateView
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.urls import reverse_lazy
from rest_framework import generics

from . import serializers as s
from . import models as m


class ProductType_list_create_api(generics.ListCreateAPIView):
    queryset = m.ProductType.objects.order_by("show_order")
    serializer_class = s.ProductType_serializer


class Product_list_create_api(generics.ListCreateAPIView):
    queryset = m.Product.objects.all()
    serializer_class = s.Product_serializer


class ProductComposition_list_create_api(generics.ListCreateAPIView):
    queryset = m.ProductComposition.objects.all()
    serializer_class = s.ProductComposition_serializer
