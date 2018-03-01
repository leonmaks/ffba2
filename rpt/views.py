from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.db import connection


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
            " SUM(tl.price) AS actual_sales_value,"
            " SUM(tl.units * p.pricesell) - SUM(tl.price) AS lost_sales_value"
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
