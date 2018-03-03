from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.db import connection

from . import data as d


class SalesDataByOrgUnit(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = ("rpt.xxx")

    template_name = "rpt/sales_data_by_org_unit.html"

    def fetch_data(self):

        stmt_ = [(
            "SELECT r.id, l.identity, max(l.create_dt) last_repl_dt"
            " FROM ffba_cashreg r, ffba_cashreg_log l"
            " WHERE r.identity = l.identity"
            " GROUP BY l.identity, r.id"
        ), ]

        with connection.cursor() as cursor:
            cursor.execute(" ".join(stmt_))
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

    def get(self, request, *args, **kwargs):
        # context = self.get_context_data(object=self.object)
        return self.render_to_response({"object_list": self.fetch_data()})


class DailySales(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = ("rpt.xxx")

    template_name = "rpt/daily_sales.html"

    def get_context_data(self, **kwargs):

        daily_sales_ = d.daily_sales()

        object_list_ = []
        sales_ = {}
        for s_ in daily_sales_:

            if not sales_ or not sales_["sales_date"] == s_["sales_date"]:
                sales_ = {
                    "sales_date": s_["sales_date"],
                    "expected_sales_value": 0,
                    "actual_sales_value": 0,
                    "lost_sales_value": 0,
                    "cashreg_recs": [],
                }
                object_list_.append(sales_)

            sales_["expected_sales_value"] += s_["expected_sales_value"]
            sales_["actual_sales_value"] += s_["actual_sales_value"]
            sales_["lost_sales_value"] += s_["lost_sales_value"]
            sales_["cashreg_recs"].append(s_)

        ctx_ = {
            "object_list": object_list_,
        }

        return super().get_context_data(**ctx_)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))


class ProductDaySales(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = ("rpt.xxx")

    template_name = "rpt/product_day_sales.html"

    def get_context_data(self, **kwargs):
        date_ = date(int(kwargs["year"]), int(kwargs["month"]), int(kwargs["mday"]))

        cashreg_ = d.cashreg(kwargs["cashreg_id"])
        object_list_ = d.product_day_sales(cashreg_["siteguid"], date_)

        ctx_ = {
            "cashreg": cashreg_,
            "sales_date": date_,
            "object_list": object_list_,
        }

        return super().get_context_data(**ctx_)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))
