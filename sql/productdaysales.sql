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



select * from ffba_cashreg;
