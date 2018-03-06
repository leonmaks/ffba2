select * from r$u001_categories;

select * from ffba_cashreg;


select * from r$u003_categories;
2a502e42-f359-4174-8a5a-46118f4637a6;

select * from r$u004_categories;
87011394-b5a6-46bf-b332-ca2f78b569f1;

select * from r$u005_categories;
34892ae3-3656-4601-92a3-16ba73b14dcb;


select * from r$d003_categories;
select * from r$u003_categories where r$_create_dt >= '2017-11-28';


select * from r$d004_categories;
insert into r$d004_categories (id, name, parentid, texttip, catshowname, image, colour, catorder, siteguid, sflag, r$_op, r$_create_dt)
  select id, name, parentid, texttip, catshowname, image, colour, catorder, '87011394-b5a6-46bf-b332-ca2f78b569f1', sflag, r$_op, now() from r$u003_categories where r$_create_dt >= '2017-11-28';


select * from r$d005_categories;
insert into r$d005_categories (id, name, parentid, texttip, catshowname, image, colour, catorder, siteguid, sflag, r$_op, r$_create_dt)
  select id, name, parentid, texttip, catshowname, image, colour, catorder, '34892ae3-3656-4601-92a3-16ba73b14dcb', sflag, r$_op, now() from r$u003_categories where r$_create_dt >= '2017-11-28';



select * from r$u003_products where r$_create_dt >= '2017-11-28';
select count(*) from r$u003_products where r$_create_dt >= '2017-11-28';


select * from r$d004_products order by r$_id;
insert into r$d004_products (id, reference, code, codetype, name, pricebuy, pricesell, category, taxcat, attributeset_id, stockcost, stockvolume, iscom, isscale, iskitchen, printkb, sendstatus, isservice, display, attributes, isvprice, isverpatrib, texttip, warranty, image, stockunits, ALIAS, alwaysavailable, discounted, candiscount, iscatalog, catorder, ispack, packquantity, packproduct, promotionid, allproducts, managestock, siteguid, sflag, r$_op, r$_create_dt)
  select id, reference, code, codetype, name, pricebuy, pricesell, category, taxcat, attributeset_id, stockcost, stockvolume, iscom, isscale, iskitchen, printkb, sendstatus, isservice, display, attributes, isvprice, isverpatrib, texttip, warranty, image, stockunits, ALIAS, alwaysavailable, discounted, candiscount, iscatalog, catorder, ispack, packquantity, packproduct, promotionid, allproducts, managestock, '87011394-b5a6-46bf-b332-ca2f78b569f1', sflag, r$_op, now() from r$u003_products where r$_create_dt >= '2017-11-28'

select * from r$d004_products_1;
select count(*) from r$d004_products_1;
create table r$d004_products_1 as select * from r$d004_products where r$_create_dt >= '2017-11-28';
delete from r$d004_products where r$_create_dt >= '2017-11-28';


select * from r$d005_products order by r$_id;
insert into r$d005_products (id, reference, code, codetype, name, pricebuy, pricesell, category, taxcat, attributeset_id, stockcost, stockvolume, iscom, isscale, iskitchen, printkb, sendstatus, isservice, display, attributes, isvprice, isverpatrib, texttip, warranty, image, stockunits, ALIAS, alwaysavailable, discounted, candiscount, iscatalog, catorder, ispack, packquantity, packproduct, promotionid, allproducts, managestock, siteguid, sflag, r$_op, r$_create_dt)
  select id, reference, code, codetype, name, pricebuy, pricesell, category, taxcat, attributeset_id, stockcost, stockvolume, iscom, isscale, iskitchen, printkb, sendstatus, isservice, display, attributes, isvprice, isverpatrib, texttip, warranty, image, stockunits, ALIAS, alwaysavailable, discounted, candiscount, iscatalog, catorder, ispack, packquantity, packproduct, promotionid, allproducts, managestock, '34892ae3-3656-4601-92a3-16ba73b14dcb', sflag, r$_op, now() from r$u003_products where r$_create_dt >= '2017-11-28'

select * from r$d005_products_1;
create table r$d005_products_1 as select * from r$d005_products where r$_create_dt >= '2017-11-28';
select count(*) from r$d005_products_1;
delete from r$d005_products where r$_create_dt >= '2017-11-28';


select * from r$u003_stockcurrent where r$_create_dt >= '2017-11-28';
select count(*) from r$u003_stockcurrent where r$_create_dt >= '2017-11-28';


select * from r$d004_stockcurrent order by r$_id;
insert into r$d004_stockcurrent (location, product, attributesetinstance_id, units, siteguid, sflag, r$_op, r$_create_dt)
  select location, product, attributesetinstance_id, units, '87011394-b5a6-46bf-b332-ca2f78b569f1', sflag, r$_op, now() from r$u003_stockcurrent where r$_create_dt >= '2017-11-28';


select * from r$d005_stockcurrent order by r$_id;
insert into r$d005_stockcurrent (location, product, attributesetinstance_id, units, siteguid, sflag, r$_op, r$_create_dt)
  select location, product, attributesetinstance_id, units, '34892ae3-3656-4601-92a3-16ba73b14dcb', sflag, r$_op, now() from r$u003_stockcurrent where r$_create_dt >= '2017-11-28';
