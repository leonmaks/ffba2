CREATE OR REPLACE VIEW "v$_product_sales_raw"
AS SELECT r.datenew AS sales_date,
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
        END AS fractional_flag,
    pm.payment
   FROM "r$_receipts" r,
    "r$_tickets" t,
    "r$_ticketlines" tl,
    "r$_products" p,
    "r$_payments" pm
  WHERE r.id::text = t.id::text AND r.siteguid::text = t.siteguid::text AND t.id::text = tl.ticket::text AND t.siteguid::text = tl.siteguid::text AND tl.product::text = p.id::text AND tl.siteguid::text = p.siteguid::text AND pm.receipt::text = r.id::text
;

ALTER TABLE public."v$_product_sales_raw" OWNER TO username;
GRANT ALL ON TABLE public."v$_product_sales_raw" TO username;
