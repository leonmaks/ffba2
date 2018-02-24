from django.urls import path

from . import views as v


app_name = "prod"

urlpatterns = [
    path(r"product-type-list/", v.ProductTypeList.as_view(), name='product-type-list'),
    path(r"product-type-create/", v.ProductTypeCreate.as_view(), name='product-type-create'),
    path(r"product-type-update/<int:pk>/", v.ProductTypeUpdate.as_view(), name="product-type-update"),
    path(r"product-list/", v.ProductList.as_view(), name='product-list'),
    path(r"product-create/", v.ProductCreate.as_view(), name='product-create'),
    path(r"product-update/<int:pk>/", v.ProductUpdate.as_view(), name="product-update"),
    path(r"product-composition-edit/", v.ProductCompositionEdit.as_view(), name="product-composition-edit"),
    path(r"product-composition-edit/<int:pk>/", v.ProductCompositionEdit.as_view(), name="product-composition-edit"),
]
