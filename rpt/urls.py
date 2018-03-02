from django.urls import path

from . import views as v


app_name = "rpt"

urlpatterns = [
    path(r"sales-data-by-org-unit/", v.SalesDataByOrgUnit.as_view(), name="sales-data-by-org-unit"),
    path(r"daily-sales/", v.DailySales.as_view(), name="daily-sales"),
    path(r"<int:year>/<int:month>/<int:mday>/product-day-sales/<int:cashreg_id>/", v.ProductDaySales.as_view(), name="product-day-sales"),
]
