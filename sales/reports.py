from datetime import date
from math import floor, ceil
from operator import itemgetter

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


class DaySales(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = ("rpt.xxx")

    template_name = "rpt/day_sales.html"

    def get_context_data(self, **kwargs):
        date_ = date(int(kwargs["year"]), int(kwargs["month"]), int(kwargs["mday"]))
        cashreg_ = d.cashreg(kwargs["cashreg_id"])

        day_sales_detail_ = d.day_sales_detail(cashreg_["siteguid"], date_)

        product_day_sales_ = []
        sales_ = {}
        totals_ = {
            "units": 0,
            "actual_sales_value": 0,
            "expected_sales_value": 0,
            "dscn_lost_sales_value": 0,
            "fractional_units": 0,
            "fractional_actual_sales_value": 0,
            "fractional_expected_sales_value": 0,
            "fractional_lost_sales_value": 0,
        }
        for d_ in day_sales_detail_:

            if not sales_ or not sales_["product_reference"] == d_["product_reference"]:
                sales_ = {
                    "product_reference": d_["product_reference"],
                    "product_name": d_["product_name"],
                    "product_pricesell": d_["product_pricesell"],
                    "units": 0.0,
                    "actual_sales_value": 0,
                    "expected_sales_value": 0,
                    "dscn_lost_sales_value": 0,
                    "fractional_units": 0,
                    "fractional_actual_sales_value": 0,
                    "fractional_expected_sales_value": 0,
                    "fractional_lost_sales_value": 0,
                    "detail_recs": [],
                }
                product_day_sales_.append(sales_)

            units_ = d_["units"]
            if units_ - floor(units_) > 0:

                units_ = fractional_units_ = ceil(units_)
                fractional_expected_sales_value_ = fractional_units_ * d_["product_pricesell"]
                fractional_lost_sales_value_ = fractional_expected_sales_value_ - d_["actual_sales_value"]

                d_["units"] = units_
                d_["fractional_units"] = fractional_units_
                d_["fractional_expected_sales_value"] = fractional_expected_sales_value_
                d_["fractional_actual_sales_value"] = d_["actual_sales_value"]
                d_["fractional_lost_sales_value"] = fractional_lost_sales_value_

                d_["expected_sales_value"] = d_["fractional_expected_sales_value"]
                d_["dscn_lost_sales_value"] = 0

                sales_["fractional_units"] += fractional_units_
                sales_["fractional_expected_sales_value"] += fractional_expected_sales_value_
                sales_["fractional_actual_sales_value"] += d_["actual_sales_value"]
                sales_["fractional_lost_sales_value"] += fractional_lost_sales_value_

                totals_["fractional_units"] += fractional_units_
                totals_["fractional_expected_sales_value"] += fractional_expected_sales_value_
                totals_["fractional_actual_sales_value"] += d_["actual_sales_value"]
                totals_["fractional_lost_sales_value"] += fractional_lost_sales_value_

            else:

                d_["expected_sales_value"] = d_["product_pricesell"] * units_
                d_["dscn_lost_sales_value"] = d_["expected_sales_value"] - d_["actual_sales_value"]

                d_["fractional_units"] = 0
                d_["fractional_expected_sales_value"] = 0
                d_["fractional_actual_sales_value"] = 0
                d_["fractional_lost_sales_value"] = 0

            d_["dscn_rate"] = 100 - (d_["actual_sales_value"] / d_["expected_sales_value"] * 100)

            sales_["units"] += units_
            sales_["actual_sales_value"] += d_["actual_sales_value"]
            sales_["expected_sales_value"] += d_["expected_sales_value"]
            sales_["dscn_lost_sales_value"] += d_["dscn_lost_sales_value"]
            sales_["detail_recs"].append(d_)

            totals_["units"] += units_
            totals_["actual_sales_value"] += d_["actual_sales_value"]
            totals_["expected_sales_value"] += d_["expected_sales_value"]
            totals_["dscn_lost_sales_value"] += d_["dscn_lost_sales_value"]

        ctx_ = {
            "cashreg": cashreg_,
            "sales_date": date_,
            "totals": totals_,
            "product_day_sales":
                # Sort list of dictionaries by values of the dictionary:
                # https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
                sorted(product_day_sales_, key=itemgetter("actual_sales_value"), reverse=True),
            "day_sales_recs":
                sorted(day_sales_detail_, key=itemgetter("sales_date")),
        }

        return super().get_context_data(**ctx_)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))


# class DaySales(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
#     permission_required = ("rpt.xxx")

#     template_name = "rpt/product_day_sales.html"

#     def get_context_data(self, **kwargs):
#         date_ = date(int(kwargs["year"]), int(kwargs["month"]), int(kwargs["mday"]))

#         cashreg_ = d.cashreg(kwargs["cashreg_id"])
#         product_day_sales_ = d.product_day_sales(cashreg_["siteguid"], date_)

#         product_day_sales_fractional_units_ = d.product_day_sales_fractional_units(cashreg_["siteguid"], date_)

#         ctx_ = {
#             "cashreg": cashreg_,
#             "sales_date": date_,
#             "product_day_sales": product_day_sales_,
#             "product_day_sales_fractional_units": product_day_sales_fractional_units_,
#         }

#         return super().get_context_data(**ctx_)

#     def get(self, request, *args, **kwargs):
#         return self.render_to_response(self.get_context_data(**kwargs))
