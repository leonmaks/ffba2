from django.urls import path, re_path
from django.views.generic import TemplateView

from . import reports as r
from . import api as api
from . import app as app


app_name = "sales"

urlpatterns = [
    path(r"sales-data-by-org-unit/", r.SalesDataByOrgUnit.as_view(), name="sales-data-by-org-unit"),
    path(r"totals-by-date/", r.TotalsByDate.as_view(), name="totals-by-date"),
    path(r"date-cashreg/<int:year>/<int:month>/<int:mday>/<int:cashreg_id>/", r.DaySales.as_view(), name="date-cashreg"),
    re_path("^daily-totals-for-period-api/((((?P<y_0>[0-9]{4})\.)?(?P<m_0>[0-9]{2})\.)?(?P<d_0>[0-9]{2})(-(((?P<y_1>[0-9]{4})\.)?(?P<m_1>[0-9]{2})\.)?(?P<d_1>[0-9]{2}))?)?$", api.DailyTotalsForPeriod.as_view()),
    # path("daily-totals-for-period-api/<int:y_0>.<int:m_0>.<int:d_0>", api.DailyTotalsForPeriod.as_view()),
    # path("daily-totals-for-period-api", api.DailyTotalsForPeriod.as_view()),
    path(r"", app.Sales.as_view(template_name="sales.html"), name="sales"),
]
