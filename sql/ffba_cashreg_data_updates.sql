select *
  from ffba_cashreg_repl_table
 where last_upld_srv_dt >= '2018-03-06 00:00:00' 
   and cashreg_id = 3
;

sharedtickets
draweropened	1
lineremoved

++
products	11	/* только обновления */
resources	5	/* обновление картинок? */

--
promotions	0
;


select * from ffba_cashreg;

4	eltapos_002
3	eltapos_001
5	eltapos_003
;


/*
 * products
 */
select *
  from r$u003_products
 where r$_create_dt >= '2018-03-06 16:00'
   and promotionid is null
 order by r$_op
;
select count(*)
  from r$u003_products
 where r$_create_dt >= '2018-03-06 16:00'
   and promotionid is null
;
11
;


select * from r$d004_products
 where "r$_create_dt" >= '2018-03-06 16:00'
 order by r$_id
;
select count(*)
  from r$d004_products
 where "r$_create_dt" >= '2018-03-06 16:00'
;

insert into r$d004_products (
    id, reference, code, codetype, name, pricebuy, pricesell, category, taxcat, attributeset_id, stockcost, stockvolume, iscom, isscale, iskitchen, printkb, sendstatus, isservice, display, attributes, isvprice, isverpatrib, texttip, warranty, image, stockunits, ALIAS, alwaysavailable, discounted, candiscount, iscatalog, catorder, ispack, packquantity, packproduct, promotionid, allproducts, managestock, siteguid, sflag, r$_op, r$_create_dt
  )
  select
    id, reference, code, codetype, name, pricebuy, pricesell, category, taxcat, attributeset_id, stockcost, stockvolume, iscom, isscale, iskitchen, printkb, sendstatus, isservice, display, attributes, isvprice, isverpatrib, texttip, warranty, image, stockunits, ALIAS, alwaysavailable, discounted, candiscount, iscatalog, catorder, ispack, packquantity, packproduct, promotionid, allproducts, managestock, '87011394-b5a6-46bf-b332-ca2f78b569f1', sflag, r$_op, now()
    from r$u003_products
 where r$_create_dt >= '2018-03-06 16:00'
   and promotionid is null
;

select *
  from r$d005_products
 where r$_create_dt >= '2018-03-06'
  order by r$_id
;
insert into r$d005_products (
    id, reference, code, codetype, name, pricebuy, pricesell, category, taxcat, attributeset_id, stockcost, stockvolume, iscom, isscale, iskitchen, printkb, sendstatus, isservice, display, attributes, isvprice, isverpatrib, texttip, warranty, image, stockunits, ALIAS, alwaysavailable, discounted, candiscount, iscatalog, catorder, ispack, packquantity, packproduct, promotionid, allproducts, managestock, siteguid, sflag, r$_op, r$_create_dt
  )
  select
    id, reference, code, codetype, name, pricebuy, pricesell, category, taxcat, attributeset_id, stockcost, stockvolume, iscom, isscale, iskitchen, printkb, sendstatus, isservice, display, attributes, isvprice, isverpatrib, texttip, warranty, image, stockunits, ALIAS, alwaysavailable, discounted, candiscount, iscatalog, catorder, ispack, packquantity, packproduct, promotionid, allproducts, managestock, '34892ae3-3656-4601-92a3-16ba73b14dcb', sflag, r$_op, now()
    from r$u003_products
 where r$_create_dt >= '2018-03-06 16:00'
   and promotionid is null
;



/*
 * PROMOTIONS
 */
select * from r$u003_promotions where r$_create_dt >= '2018-03-06';
select count(*) from r$u003_promotions where r$_create_dt >= '2018-03-06';

3
;



/*
 * resources
 */
select *
  from r$u003_resources
 where r$_create_dt >= '2018-03-06 16:00'
;
select count(*)
  from r$u003_resources
 where r$_create_dt >= '2018-03-06 16:00'
;

1
;


select *
  from r$d004_resources
 order by r$_id
;
select count(*)
  from r$d004_resources
;
5
;

insert into r$d004_resources (
    id, name, restype, content, siteguid, sflag, r$_op, r$_create_dt
  )
  select
    id, name, restype, content, '87011394-b5a6-46bf-b332-ca2f78b569f1', sflag, r$_op, now()
    from r$u003_resources
 where r$_create_dt >= '2018-03-06 16:00'
;

select *
  from r$d005_resources
 order by r$_id
;
select count(*)
  from r$d005_resources
;
insert into r$d005_resources (
    id, name, restype, content, siteguid, sflag, r$_op, r$_create_dt
  )
  select
    id, name, restype, content, '34892ae3-3656-4601-92a3-16ba73b14dcb', sflag, r$_op, now()
    from r$u003_resources
 where r$_create_dt >= '2018-03-06 16:00'
;



/*
 * DRAWEROPENED
 */
select * from r$u003_draweropened where r$_create_dt >= '2018-03-06';
select count(*) from r$u003_draweropened where r$_create_dt >= '2018-03-06';

1
;



/*
 * sharedtickets
 */
select * from r$u003_sharedtickets where r$_create_dt >= '2018-03-06' order by "r$_create_dt"
;
select count(*) from r$u003_sharedtickets where r$_create_dt >= '2018-03-06'
;

select r$_op, count(*)
  from r$u003_sharedtickets
 group by r$_op
;


select st.*
  from r$u003_sharedtickets st
 where st.r$_op = 'N'
   and r$_create_dt >= '2018-03-06'
   and not exists (
     select 1
       from r$u003_sharedtickets st2
      where st2.id = st.id
        and st2.name = st.name
        and st2.content = st.content
        and st2.pickupid = st.pickupid
        and st2.appuser = st.appuser
        and st.r$_op = 'D'
        and r$_create_dt >= '2018-03-06'
   )
;



/*
 * lineremoved
 */
select * from r$u003_lineremoved where r$_create_dt >= '2018-03-06' order by "r$_create_dt"
;
select count(*) from r$u003_lineremoved where r$_create_dt >= '2018-03-06'
;




/*
 * 
 */
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


select * from r$d005_products order by r$_id;
insert into r$d005_products (id, reference, code, codetype, name, pricebuy, pricesell, category, taxcat, attributeset_id, stockcost, stockvolume, iscom, isscale, iskitchen, printkb, sendstatus, isservice, display, attributes, isvprice, isverpatrib, texttip, warranty, image, stockunits, ALIAS, alwaysavailable, discounted, candiscount, iscatalog, catorder, ispack, packquantity, packproduct, promotionid, allproducts, managestock, siteguid, sflag, r$_op, r$_create_dt)
  select id, reference, code, codetype, name, pricebuy, pricesell, category, taxcat, attributeset_id, stockcost, stockvolume, iscom, isscale, iskitchen, printkb, sendstatus, isservice, display, attributes, isvprice, isverpatrib, texttip, warranty, image, stockunits, ALIAS, alwaysavailable, discounted, candiscount, iscatalog, catorder, ispack, packquantity, packproduct, promotionid, allproducts, managestock, '34892ae3-3656-4601-92a3-16ba73b14dcb', sflag, r$_op, now() from r$u003_products where r$_create_dt >= '2017-11-28'



select * from r$u003_stockcurrent where r$_create_dt >= '2017-11-28';
select count(*) from r$u003_stockcurrent where r$_create_dt >= '2017-11-28';


select * from r$d004_stockcurrent order by r$_id;
insert into r$d004_stockcurrent (location, product, attributesetinstance_id, units, siteguid, sflag, r$_op, r$_create_dt)
  select location, product, attributesetinstance_id, units, '87011394-b5a6-46bf-b332-ca2f78b569f1', sflag, r$_op, now() from r$u003_stockcurrent where r$_create_dt >= '2017-11-28';


select * from r$d005_stockcurrent order by r$_id;
insert into r$d005_stockcurrent (location, product, attributesetinstance_id, units, siteguid, sflag, r$_op, r$_create_dt)
  select location, product, attributesetinstance_id, units, '34892ae3-3656-4601-92a3-16ba73b14dcb', sflag, r$_op, now() from r$u003_stockcurrent where r$_create_dt >= '2017-11-28';
