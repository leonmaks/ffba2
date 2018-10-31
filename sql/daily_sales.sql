
SELECT s.sales_date::date AS sales_date,
 cr.identity AS cashreg_ident,
 s.payment AS payment,
 SUM(s.expected_sales_value) AS exp_sv,
 SUM(s.actual_sales_value) AS act_sv,
 SUM(s.discount_value) AS dis_sv
 FROM ffba_cashreg cr, v$_product_sales s
 WHERE cr.siteguid = s.siteguid
 GROUP BY s.sales_date::date, coalesce(cr.show_order, cr.identity), cr.identity, s.payment
 ORDER BY s.sales_date::date DESC, coalesce(cr.show_order, cr.identity), s.payment
;
