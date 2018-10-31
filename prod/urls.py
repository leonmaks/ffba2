from django.urls import path
from django.views.generic import TemplateView

from . import views as v
from . import api


app_name = "prod"

urlpatterns = [
    path(r"product-type-list/", v.ProductTypeList.as_view(), name="product-type-list"),
    path(r"product-type-list-create-api/", api.ProductType_list_create_api.as_view(), name="product-type-list-create-api"),
    path(r"product-type-create/", v.ProductTypeCreate.as_view(), name="product-type-create"),
    path(r"product-type-update/<int:pk>/", v.ProductTypeUpdate.as_view(), name="product-type-update"),
    path(r"product-list/", v.ProductList.as_view(), name="product-list"),
    path(r"product-list-create-api/", api.Product_list_create_api.as_view(), name="product-list-create-api"),
    path(r"product-create/", v.ProductCreate.as_view(), name="product-create"),
    path(r"product-update/<int:pk>/", v.ProductUpdate.as_view(), name="product-update"),
    path(r"product-composition-list/", v.ProductCompositionList.as_view(), name="product-composition-list"),
    path(r"product-composition-list-create-api/", api.ProductComposition_list_create_api.as_view(), name="product-composition-list-create-api"),
    path(r"product-composition-create/", v.ProductCompositionCreate.as_view(), name="product-composition-create"),
    path(r"product-composition-app/", TemplateView.as_view(template_name="prod/product-composition-app.html"), name="product-composition-app"),
    # path(r"product-composition-edit/<int:pk>/", v.ProductCompositionEdit.as_view(), name="product-composition-edit"),
]
