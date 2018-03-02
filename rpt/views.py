from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.db import connection

from datetime import date


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

    def fetch_data(self):

        stmt_ = [(
            "SELECT cr.identity AS cashreg_identity,"
            " cr.id cashreg_id,"
            " r.datenew::date sales_date,"
            " SUM(tl.units * p.pricesell) AS expected_sales_value,"
            " SUM(tl.units * tl.price) AS actual_sales_value,"
            " SUM(tl.units * p.pricesell) - SUM(tl.units * tl.price) AS lost_sales_value"
            " FROM r$_products p, r$_ticketlines tl, r$_receipts r, ffba_cashreg cr"
            " WHERE r.siteguid = cr.siteguid"
            " AND tl.ticket = r.id AND tl.siteguid = r.siteguid"
            " AND p.id = tl.product AND p.siteguid = r.siteguid"
            " GROUP BY cashreg_identity, cashreg_id, sales_date"
            " ORDER BY sales_date DESC, cashreg_identity ASC"
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


class ProductDaySales(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = ("rpt.xxx")

    template_name = "rpt/product_day_sales.html"

    def get_context_data(self, **kwargs):
        date_ = date(int(kwargs["year"]), int(kwargs["month"]), int(kwargs["mday"]))
        ctx_ = {
            "cashreg": fetch_cashreg_data(kwargs["cashreg_id"]),
            "sales_date": date_,
            "object_list": fetch_product_day_sales(kwargs["cashreg_id"], date_),
        }
        return super().get_context_data(**ctx_)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))


def fetch_cashreg_data(cashreg_id):

    stmt_ = (
        "SELECT cr.id, cr.identity, cr.siteguid"
        " FROM ffba_cashreg cr"
        " WHERE cr.id = %s"
    )

    with connection.cursor() as cursor:
        cursor.execute(stmt_, (cashreg_id, ))
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ][0]


def fetch_product_day_sales(cashreg_id, mday):

    stmt_ = (
        "SELECT p.reference AS product_reference,"
        " p.name AS product_name,"
        " p.pricesell AS product_pricesell,"
        " SUM(tl.units) AS units,"
        " SUM(tl.units * p.pricesell) AS expected_sales_value,"
        " SUM(tl.units * tl.price) AS actual_sales_value,"
        " SUM(tl.units * p.pricesell) - SUM(tl.units * tl.price) AS lost_sales_value"
        " FROM ffba_cashreg cr, r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p"
        " WHERE cr.id = %s"
        " AND cr.siteguid = r.siteguid"
        " AND r.id = t.id AND r.siteguid = t.siteguid"
        " AND t.id = tl.ticket AND t.siteguid = tl.siteguid"
        " AND tl.product = p.id AND tl.siteguid = p.siteguid"
        " AND r.datenew::date = %s"
        " GROUP BY product_reference, product_name, product_pricesell"
        " ORDER BY actual_sales_value DESC"
    )

    with connection.cursor() as cursor:
        cursor.execute(stmt_, (cashreg_id, mday))
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
