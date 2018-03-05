
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


