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
 WHERE r.datenew::date = '2018-03-01'
 GROUP BY tl.product, p.reference, p.name, p.pricebuy, p.pricesell
 ORDER BY expected_sales_value DESC
;

SELECT * from r$_receipts
;
SELECT * from r$_payments
;
