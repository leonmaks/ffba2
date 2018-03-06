from django.urls import path

from . import reports as r


app_name = "sales"

urlpatterns = [
    path(r"sales-data-by-org-unit/", r.SalesDataByOrgUnit.as_view(), name="sales-data-by-org-unit"),
    path(r"daily-sales/", r.DailySales.as_view(), name="daily-sales"),
    path(r"<int:year>/<int:month>/<int:mday>/day-sales/<int:cashreg_id>/", r.DaySales.as_view(), name="day-sales"),
]
