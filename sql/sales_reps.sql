-- Totals by DATE, CASHREG

SELECT cr.identity AS cashreg_identity,
 cr.id AS cashreg_id,
 s.sales_date::date AS sdate,
 s.payment,
 SUM(s.expected_sales_value) AS expected_sales_value,
 SUM(s.actual_sales_value) AS actual_sales_value,
 SUM(s.discount_value) AS discount_value
 FROM ffba_cashreg cr, v$_product_sales s
 WHERE cr.siteguid = s.siteguid
 GROUP BY cashreg_identity, cashreg_id, cr.show_order, sdate, s.payment
 ORDER BY sdate DESC, coalesce(cr.show_order, cr.identity)
;

EXPLAIN ANALYZE;
SELECT cr.identity AS cashreg_identity,
    cr.id AS cashreg_id,
    s.sales_date::date AS sdate,
    SUM(s.expected_sales_value) AS expected_sales_value,
    SUM(s.actual_sales_value) AS actual_sales_value,
    SUM(s.discount_value) AS discount_value
  FROM ffba_cashreg cr, v$_product_sales s
  WHERE cr.siteguid = s.siteguid
    AND s.sales_date::date >= '2018-01-01'
    AND s.sales_date::date <= '2018-08-01'
  GROUP BY cashreg_identity, cashreg_id, cr.show_order, sdate
  ORDER BY sdate DESC, coalesce(cr.show_order, cr.identity)
;

EXPLAIN ANALYZE
SELECT cr.identity AS cashreg_identity,
    cr.id AS cashreg_id,
    s.sales_date::date AS sdate,
    SUM(s.expected_sales_value) AS expected_sales_value,
    SUM(s.actual_sales_value) AS actual_sales_value,
    SUM(s.discount_value) AS discount_value
  FROM ffba_cashreg cr, v$_product_sales s
  WHERE cr.siteguid = s.siteguid
  GROUP BY cashreg_identity, cashreg_id, cr.show_order, sdate
  ORDER BY sdate DESC, coalesce(cr.show_order, cr.identity)
;

SELECT r.datenew AS sales_date,
    r.siteguid,
    p.reference AS product_ref,
    p.name AS product_name,
    tl.units,
    ceil(tl.units) AS total_units,
    p.pricesell AS list_price,
    tl.price AS actual_price,
        CASE
            WHEN ceil(tl.units - floor(tl.units)) <> 0::double precision THEN true
            ELSE false
        END AS fractional_flag
   FROM "r$_receipts" r,
    "r$_tickets" t,
    "r$_ticketlines" tl,
    "r$_products" p
  WHERE r.id::text = t.id::text
    AND r.siteguid::text = t.siteguid::text
    AND t.id::text = tl.ticket::text
    AND t.siteguid::text = tl.siteguid::text
    AND tl.product::text = p.id::text
    AND tl.siteguid::text = p.siteguid::text
;

select * from r$_ticketlines;
select distinct payment from r$_payments;
