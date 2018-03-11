

SELECT s.siteguid, s.product_ref, s.product_name, s.sales_date,
 s.units, s.total_units, s.fractional_flag,
 s.total_units * s.price_sell AS expected_sales_value,
 s.units * s.price_sold AS actual_sales_value,
 s.total_units * s.price_sell - s.units * s.price_sold AS discount_value,
 (s.units * s.price_sold) / (s.total_units * s.price_sell) AS discount_rate
 FROM v$_product_sales_raw s
 ORDER BY sales_date DESC
;


units
actual_sales_value
expected_sales_value
lost_sales_value

discount_value
discount_rate

fractional_units
fractional_actual_sales_value
fractional_expected_sales_value
fractional_lost_sales_value
;


SELECT *
 FROM v$_product_sales
 WHERE fractional_flag
;


SELECT DATE(s.sales_date) AS sd, s.siteguid AS sg,
 SUM(s.expected_sales_value) AS expected_sales_value,
 SUM(s.actual_sales_value) AS actual_sales_value,
 SUM(s.discount_value) AS discount_value
 FROM v$_product_sales s
 GROUP BY sd, sg
 ORDER BY sd DESC, sg
;


DROP VIEW v$_product_sales_raw
;


CREATE OR REPLACE VIEW v$_product_sales_raw AS
 SELECT r.datenew sales_date, r.siteguid, p.reference AS product_ref, p.name AS product_name,
 tl.units AS units, ceil(tl.units) total_units, p.pricesell AS list_price, tl.price AS actual_price,
 CASE WHEN ceil(tl.units - floor(tl.units)) != 0 THEN TRUE ELSE FALSE END AS fractional_flag
 FROM r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p
 WHERE r.id = t.id AND r.siteguid = t.siteguid
 AND t.id = tl.ticket AND t.siteguid = tl.siteguid
 AND tl.product = p.id AND tl.siteguid = p.siteguid
;


DROP VIEW v$_product_sales
;


CREATE OR REPLACE VIEW v$_product_sales AS
SELECT s.siteguid, s.product_ref, s.product_name, s.sales_date,
 s.units, s.total_units, s.list_price, s.actual_price, s.fractional_flag,
 s.total_units * s.list_price AS expected_sales_value,
 s.units * s.actual_price AS actual_sales_value,
 s.total_units * s.list_price - s.units * s.actual_price AS discount_value,
 CASE WHEN s.total_units != 0 AND s.list_price != 0 THEN (s.units * s.actual_price) / (s.total_units * s.list_price) ELSE -1 END AS discount_rate
 FROM v$_product_sales_raw s
;


SELECT s.sales_date,
    s.siteguid,
    s.product_name,
    s.product_ref,
    s.units,
    s.fractional_flag
           ceil(tl.units - floor(tl.units)) * floor(tl.units) fractional_units
 FROM (
    SELECT r.datenew sales_date,
           r.siteguid,
           p.reference AS product_ref,
           p.name AS product_name,
           ceil(tl.units) AS units,
           p.pricesell AS pricesell,
           tl.units * tl.price AS actual_sales_value,
           ceil(tl.units - floor(tl.units)) fractional_flag
     FROM r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p
     WHERE r.id = t.id AND r.siteguid = t.siteguid
     AND t.id = tl.ticket AND t.siteguid = tl.siteguid
     AND tl.product = p.id AND tl.siteguid = p.siteguid
 ) AS s
WHERE s.fractional_flag != 0
 ORDER BY sales_date DESC
;



units
actual_sales_value
expected_sales_value
lost_sales_value

discount_value
discount_rate

fractional_units
fractional_actual_sales_value
fractional_expected_sales_value
fractional_lost_sales_value





select * from "r$_ticketlines";


SELECT
    r.datenew sales_date,
    r.siteguid,
    p.reference AS product_ref,
    p.name AS product_name,
    ceil(tl.units) AS units,
    p.pricesell AS pricesell,
    tl.units * tl.price AS actual_sales_value,
    ceil(tl.units - floor(tl.units)) * floor(tl.units) fractional_units
 FROM r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p
 WHERE r.id = t.id AND r.siteguid = t.siteguid
 AND t.id = tl.ticket AND t.siteguid = tl.siteguid
 AND tl.product = p.id AND tl.siteguid = p.siteguid
-- GROUP BY sales_date, siteguid
-- ORDER BY product_reference ASC, units DESC
 AND fractional_units != 0
 ORDER BY units DESC
;


SELECT p.reference AS product_reference,
 p.name AS product_name,
 p.pricesell AS product_pricesell,
 tl.units AS units,
 tl.units * tl.price AS actual_sales_value
 FROM r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p
 WHERE r.siteguid = '87011394-b5a6-46bf-b332-ca2f78b569f1'
 AND r.datenew::date = '2018-03-01'
 AND r.id = t.id AND r.siteguid = t.siteguid
 AND t.id = tl.ticket AND t.siteguid = tl.siteguid
 AND tl.product = p.id AND tl.siteguid = p.siteguid
 ORDER BY product_reference ASC, units DESC
;


/*
 * Продажи за день,
 * в которых количество (units)
 * имеет ненулевое дробное значение.
 */
EXPLAIN;
SELECT p.reference AS product_reference,
 p.name AS product_name,
 p.pricesell AS product_pricesell,
 SUM(tl.units) AS units,
 SUM(tl.units * p.pricesell) AS expected_sales_value,
 SUM(tl.units * tl.price) AS actual_sales_value,
 SUM(tl.units * p.pricesell) - SUM(tl.units * tl.price) AS lost_sales_value
 FROM r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p
 WHERE r.siteguid = '87011394-b5a6-46bf-b332-ca2f78b569f1'
 AND r.id = t.id AND r.siteguid = t.siteguid
 AND t.id = tl.ticket AND t.siteguid = tl.siteguid
 AND tl.product = p.id AND tl.siteguid = p.siteguid
 AND r.datenew::date = '2018-03-01'
 GROUP BY product_reference, product_name, product_pricesell
 ORDER BY actual_sales_value DESC
;


/*
 * Продажи за день,
 * в которых количество (units)
 * имеет ненулевое дробное значение.
 */
SELECT p.reference AS product_reference,
 p.name AS product_name,
 tl.units AS units,
 p.pricesell AS product_pricesell,
 tl.units * tl.price AS actual_sales_value
 FROM r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p
 WHERE r.siteguid = '87011394-b5a6-46bf-b332-ca2f78b569f1'
 AND r.id = t.id AND r.siteguid = t.siteguid
 AND t.id = tl.ticket AND t.siteguid = tl.siteguid
 AND tl.product = p.id AND tl.siteguid = p.siteguid
 AND tl.units - ceil(tl.units) != 0
 AND r.datenew::date = '2018-03-01'
 ORDER BY actual_sales_value DESC
;


/*
 * Продажи, в которых количество (units)
 * имеет ненулевое дробное значение и,
 * при этом, больше единицы.
 */
SELECT p.reference AS product_reference,
 p.name AS product_name,
 p.pricesell AS product_pricesell,
 tl.units,
 tl.units * tl.price AS actual_sales_value
 FROM r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p
 WHERE r.id = t.id AND r.siteguid = t.siteguid
 AND t.id = tl.ticket AND t.siteguid = tl.siteguid
 AND tl.units - ceil(tl.units) != 0
 AND ceil(tl.units) > 1
 AND tl.product = p.id AND tl.siteguid = p.siteguid
;



SELECT * FROM r$_tickets WHERE id = '6cced27e-bceb-4b8b-a27d-15f913485989'
;

SELECT * FROM r$_receipts r WHERE id = '6cced27e-bceb-4b8b-a27d-15f913485989'
;

select * from ffba_cashreg
;


