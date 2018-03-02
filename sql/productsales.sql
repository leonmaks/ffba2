SELECT p.reference,
       p.name,
       SUM(tl.units) AS units,
       SUM(tl.units * p.pricesell) AS expected_sales_value,
       SUM(tl.units * tl.price) AS actual_sales_value,
       SUM(tl.units * p.pricesell) - SUM(tl.units * tl.price) AS lost_sales_value
 FROM ffba_cashreg cr, r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p
 WHERE cr.id = 5
   AND cr.siteguid = r.siteguid
   AND r.id = t.id AND r.siteguid = t.siteguid
   AND t.id = tl.ticket AND t.siteguid = tl.siteguid
   AND tl.product = p.id AND tl.siteguid = p.siteguid
   AND r.datenew::date = DATE '2018-03-01'
 GROUP BY p.reference, p.name
 ORDER BY actual_sales_value DESC
;



SELECT p.reference AS product_reference,
 p.name AS product_name,
 SUM(tl.units) AS units,
 SUM(tl.units * p.pricesell) AS expected_sales_value,
 SUM(tl.units * tl.price) AS actual_sales_value,
 SUM(tl.units * p.pricesell) - SUM(tl.units * tl.price) AS lost_sales_value
 FROM ffba_cashreg cr, r$_receipts r, r$_tickets t, r$_ticketlines tl, r$_products p
 WHERE cr.id = 5
 AND cr.siteguid = r.siteguid
 AND r.id = t.id AND r.siteguid = t.siteguid
 AND t.id = tl.ticket AND t.siteguid = tl.siteguid
 AND tl.product = p.id AND tl.siteguid = p.siteguid
 AND r.datenew::date = DATE '2018-03-01'
 GROUP BY p.reference, p.name
 ORDER BY actual_sales_value DESC
;
