SELECT p.payment,
       SUM(p.total) AS payment_total
 FROM r$_closedcash c, r$_payments p, r$_receipts r
 WHERE c.money = r.money
   AND p.receipt = r.id
 GROUP BY p.payment
;


SELECT * FROM r$_payments p
;

SELECT * FROM r$_receipts r
;

SELECT * FROM r$_closedcash c
;



SELECT EXTRACT(HOURS FROM (dateend - datestart)) FROM r$_closedcash c WHERE money = '87c364da-453d-4b37-8333-eb5f33b89de5'
;

SELECT EXTRACT(HOURS FROM (dateend - datestart)) h, count(*)
  FROM r$_closedcash c
 GROUP BY h
 ORDER BY h
;

SELECT * FROM r$_closedcash c WHERE money = '87c364da-453d-4b37-8333-eb5f33b89de5'
;



SELECT p.*, r.*
 FROM r$_closedcash c, r$_payments p, r$_receipts r
 WHERE c.money = r.money
   AND p.receipt = r.id
   AND c.money = '87c364da-453d-4b37-8333-eb5f33b89de5'
;

SELECT cr.identity AS idn, r.datenew::date dy,
       SUM(tl.units * p.pricesell) AS expected_sales_value,
       SUM(tl.price) AS actual_sales_value,
       SUM(tl.units * p.pricesell) - SUM(tl.price) AS lost_sales_value
  FROM r$_products p, r$_ticketlines tl, r$_receipts r, ffba_cashreg cr
 WHERE r.siteguid = cr.siteguid
   AND tl.ticket = r.id AND tl.siteguid = r.siteguid
   AND p.id = tl.product AND p.siteguid = r.siteguid
 GROUP BY idn, dy
 ORDER BY dy DESC, idn ASC
;

SELECT p.reference,
       p.name,
       p.pricebuy,
       p.pricesell,
       SUM(tl.units) AS sold_units,
       SUM(tl.units * p.pricebuy) AS cost_value,
       SUM(tl.units * p.pricesell) AS expected_sales_value,
       SUM(tl.price) AS actual_sales_value,
       SUM(tl.units * p.pricesell) - SUM(tl.units * p.pricebuy) AS expected_profit,
       SUM(tl.price) - SUM(tl.units * p.pricebuy) AS actual_profit
  FROM (r$_ticketlines tl
        INNER JOIN r$_receipts r ON (tl.ticket = r.id))
        LEFT OUTER JOIN r$_products p ON (tl.product = p.id)
 WHERE r.datenew between '2018-03-01 00:00:00' and '2018-03-01 23:59:59'
 GROUP BY tl.product, p.reference, p.name, p.pricebuy, p.pricesell
 ORDER BY expected_sales_value DESC
;
