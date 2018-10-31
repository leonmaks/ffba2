from rest_framework import serializers

from . import models as m


class ProductType_serializer(serializers.ModelSerializer):
    class Meta:
        model = m.ProductType
        fields = ("id", "code", "name", "show_order",)


class Product_serializer(serializers.ModelSerializer):
    class Meta:
        model = m.Product
        fields = ("id", "code", "product_type", "name",)


class ProductComposition_serializer(serializers.ModelSerializer):
    class Meta:
        model = m.ProductComposition
        fields = ("id", "up", "product", "note", "weight_initial",)
