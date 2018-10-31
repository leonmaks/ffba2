from django.db import connection


def totals_by_date():

    stmt_ = (
        "SELECT cr.identity AS cashreg_identity,"
        " cr.id AS cashreg_id,"
        " s.sales_date::date AS sdate,"
        " SUM(s.expected_sales_value) AS expected_sales_value,"
        " SUM(s.actual_sales_value) AS actual_sales_value,"
        " SUM(s.discount_value) AS discount_value"
        " FROM ffba_cashreg cr, v$_product_sales s"
        " WHERE cr.siteguid = s.siteguid"
        " GROUP BY cashreg_identity, cashreg_id, sdate"
        " ORDER BY sdate DESC, cashreg_identity ASC"
    )

    with connection.cursor() as cursor:
        cursor.execute(stmt_)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


def daily_totals_for_period(d_0, d_1):

    stmt_ = (
        "SELECT s.sales_date::date AS sales_date,"
        " cr.identity AS cashreg_ident,"
        " cr.id AS cashreg_id,"
        " s.payment AS payment,"
        " SUM(s.expected_sales_value) AS exp_sv,"
        " SUM(s.actual_sales_value) AS act_sv,"
        " SUM(s.discount_value) AS dis_sv"
        " FROM ffba_cashreg cr, v$_product_sales s"
        " WHERE cr.siteguid = s.siteguid"
        " AND s.sales_date::date >= %s"
        " AND s.sales_date::date <= %s"
        " GROUP BY s.sales_date::date, coalesce(cr.show_order, cr.identity), cr.identity, cr.id, s.payment"
        " ORDER BY s.sales_date::date DESC, coalesce(cr.show_order, cr.identity), s.payment"
    )

    with connection.cursor() as cursor:
        cursor.execute(stmt_, (d_0, d_1))
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


def daily_sales_SAVED():

    stmt_ = (
        "SELECT cr.identity AS cashreg_identity,"
        " cr.id cashreg_id,"
        " r.datenew sales_date,"
        " SUM(tl.units * p.pricesell) AS expected_sales_value,"
        " SUM(tl.units * tl.price) AS actual_sales_value,"
        " SUM(tl.units * p.pricesell) - SUM(tl.units * tl.price) AS lost_sales_value"
        " FROM r$_products p, r$_ticketlines tl, r$_receipts r, ffba_cashreg cr"
        " WHERE r.siteguid = cr.siteguid"
        " AND tl.ticket = r.id AND tl.siteguid = r.siteguid"
        " AND p.id = tl.product AND p.siteguid = r.siteguid"
        " GROUP BY cashreg_identity, cashreg_id, sales_date"
        " ORDER BY sales_date DESC, cashreg_identity ASC"
    )

    with connection.cursor() as cursor:
        cursor.execute(stmt_)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


def cashreg(cashreg_id):

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


def product_day_sales(siteguid, mday):

    stmt_ = (
        "SELECT p.reference AS product_reference,"
        " p.name AS product_name,"
        " p.pricesell AS product_pricesell,"
        " SUM(tl.units) AS units,"
        " SUM(tl.units * p.pricesell) AS expected_sales_value,"
        " SUM(tl.units * tl.price) AS actual_sales_value,"
        " SUM(tl.units * p.pricesell) - SUM(tl.units * tl.price) AS lost_sales_value"
        " FROM r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p"
        " WHERE r.siteguid = %s"
        " AND r.id = t.id AND r.siteguid = t.siteguid"
        " AND t.id = tl.ticket AND t.siteguid = tl.siteguid"
        " AND tl.product = p.id AND tl.siteguid = p.siteguid"
        " AND r.datenew::date = %s"
        " GROUP BY product_reference, product_name, product_pricesell"
        " ORDER BY actual_sales_value DESC"
    )

    with connection.cursor() as cursor:
        cursor.execute(stmt_, (siteguid, mday))
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


def day_sales_detail(siteguid, mday):

    stmt_ = (
        "SELECT p.reference AS product_reference,"
        " p.name AS product_name,"
        " p.pricesell AS product_pricesell,"
        " tl.units AS units,"
        " tl.units * tl.price AS actual_sales_value,"
        " r.datenew sales_date"
        " FROM r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p"
        " WHERE r.siteguid = %s"
        " AND r.datenew::date = %s"
        " AND r.id = t.id AND r.siteguid = t.siteguid"
        " AND t.id = tl.ticket AND t.siteguid = tl.siteguid"
        " AND tl.product = p.id AND tl.siteguid = p.siteguid"
        " ORDER BY product_reference ASC, units DESC"
    )

    with connection.cursor() as cursor:
        cursor.execute(stmt_, (siteguid, mday))
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


def product_day_sales_fractional_units(siteguid, mday):

    stmt_ = (
        "SELECT p.reference AS product_reference,"
        " p.name AS product_name,"
        " tl.units AS units,"
        " p.pricesell AS product_pricesell,"
        " tl.units * tl.price AS actual_sales_value"
        " FROM r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p"
        " WHERE r.siteguid = %s"
        " AND r.id = t.id AND r.siteguid = t.siteguid"
        " AND t.id = tl.ticket AND t.siteguid = tl.siteguid"
        " AND tl.product = p.id AND tl.siteguid = p.siteguid"
        " AND tl.units - ceil(tl.units) != 0"
        " AND r.datenew::date = %s"
        " ORDER BY actual_sales_value DESC"
    )

    with connection.cursor() as cursor:
        cursor.execute(stmt_, (siteguid, mday))
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
