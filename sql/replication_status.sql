select * from ffba_cashreg_log where identity='eltapos_001' order by create_dt desc;
select count(*) from ffba_cashreg_log where identity='eltapos_001';
delete from ffba_cashreg_log where identity='eltapos_001' and id <= 130576;


select * from ffba_cashreg_log where identity='eltapos_002' order by create_dt desc;
select count(*) from ffba_cashreg_log where identity='eltapos_002';
delete from ffba_cashreg_log where identity='eltapos_002' and id <= 130704;


select * from ffba_cashreg_log where identity='eltapos_003' order by create_dt desc;
select count(*) from ffba_cashreg_log where identity='eltapos_003';
delete from ffba_cashreg_log where identity='eltapos_003' and id <= 130742;


select * from ffba_cashreg_log order by create_dt desc;


select * from ffba_cashreg_log where identity='eltapos_002' and level_name = 'ERROR' order by create_dt desc;

select identity, count(*) from ffba_cashreg_log group by identity;

delete from ffba_cashreg_log where identity='eltapos_001' and id <= 26712;
delete from ffba_cashreg_log where identity='eltapos_002' and id <= 20274;


delete from ffba_cashreg_log where identity='eltapos_002';
delete from ffba_cashreg_log where create_dt <= '2017-09-03 23:59:59';



CREATE TABLE ffba_cashreg_repl_table (id serial NOT NULL, table_name character varying(63) NOT NULL, last_repl_id bigint NOT NULL, last_update_dt timestamp with time zone, cashreg_id integer NOT NULL);

DELETE FROM ffba_cashreg_repl_table r WHERE r.cashreg_id = 4 AND r.table_name = 'draweropened';

grant select on ffba_cashreg_action to ffba_cashreg_role;
grant select, update on ffba_cashreg_action_exec to ffba_cashreg_role;
grant select on pg_authid to ffba_cashreg_role;
GRANT USAGE, SELECT ON SEQUENCE ffba_cashreg_repl_table_id_seq TO ffba_cashreg_role;

grant select, insert, update, delete on ffba_cashreg_repl_table to ffba_cashreg_role;


revoke select, insert, update on ffba_cashreg_action from ffba_cashreg_role;
revoke select, update on ffba_cashreg_action_exec from ffba_cashreg_role;



grant select, insert, update on ffba_cashreg_module_deploy to ffba_cashreg_role;
grant execute on FUNCTION ffba_cashreg_get_config(integer) to ffba_cashreg_role;
grant select on ffba_cashreg_config to ffba_cashreg_role;


select * from ffba_cashreg_module;
insert into ffba_cashreg_module (create_dt, name, content, status, create_user_id, root) values (now(), 'tittles.py', '', 'A', 2, false);

select * from ffba_cash_record where id >= 1262;
update ffba_cash_record set create_user_id = 12 where id >= 1262;


CREATE TABLE ffba_cashreg_config (id serial NOT NULL, create_dt timestamp with time zone NOT NULL, modify_dt timestamp with time zone, db_user_current character varying(100) NOT NULL, db_pass_current character varying(100) NOT NULL, db_name_current character varying(100) NOT NULL, db_host_current character varying(100) NOT NULL, cashreg_id integer NOT NULL, create_user_id integer NOT NULL, modify_user_id integer);
CREATE TABLE ffba_cashreg_config_history (id integer NOT NULL, create_dt timestamp with time zone NOT NULL, modify_dt timestamp with time zone, db_user_current character varying(100) NOT NULL, db_pass_current character varying(100) NOT NULL, db_name_current character varying(100) NOT NULL, db_host_current character varying(100) NOT NULL, history_id serial NOT NULL, history_date timestamp with time zone NOT NULL, history_type character varying(1) NOT NULL, cashreg_id integer, create_user_id integer, history_user_id integer, modify_user_id integer);

alter table ffba_cashreg_config set (db_name_current null, db_host_current is null);

ALTER TABLE ffba_cashreg_config_history ALTER COLUMN db_name_current DROP NOT NULL;
ALTER TABLE ffba_cashreg_config_history ALTER COLUMN db_host_current DROP NOT NULL;

CREATE OR REPLACE FUNCTION ffba_cashreg_get_config(_cashreg_id integer)
  RETURNS TABLE (
    db_user_current varchar,
    db_pass_current varchar,
    db_name_current varchar,
    db_host_current varchar)
  AS $func$
BEGIN
  RETURN QUERY
  SELECT c.db_user_current,
         c.db_pass_current,
         c.db_name_current,
         c.db_host_current
    FROM ffba_cashreg_config c
   WHERE c.cashreg_id = 4;
END
$func$ LANGUAGE plpgsql;

select * from ffba_cashreg_get_config(4);


create table "#test" (id integer);

insert into "#test" values (5);

select * from "#test";


SELECT n.nspname, c.relname,
  CASE c.relkind WHEN 'r' THEN 'table' WHEN 'v' THEN 'view' WHEN 'm' THEN 'materialized view' WHEN 'i' THEN 'index' WHEN 'S' THEN 'sequence' WHEN 's' THEN 'special' WHEN 'f' THEN 'f
oreign table' END,
  u.usename
  FROM pg_catalog.pg_user u, pg_catalog.pg_namespace n, pg_catalog.pg_class c
 WHERE n.oid = c.relnamespace
   AND u.usesysid = c.relowner
   AND n.nspname <> 'pg_catalog'
   AND n.nspname <> 'information_schema'
   AND n.nspname !~ '^pg_toast'
   AND pg_catalog.pg_table_is_visible(c.oid)
;

pg_catalog.pg_user u on (c.relowner = u.usesysid);


select count(*) from r$u003_tickets;


select to_char(r$_create_dt, 'YYYY MM DD') DT, count(*), sum(price*units) from r$u003_ticketlines group by to_char(r$_create_dt, 'YYYY MM DD') order by DT desc;
select to_char(r$_create_dt, 'YYYY MM DD') DT, count(*), sum(price*units) from r$u004_ticketlines group by to_char(r$_create_dt, 'YYYY MM DD') order by DT desc;
select to_char(r$_create_dt, 'YYYY MM DD') DT, count(*), sum(price*units) from r$u005_ticketlines group by to_char(r$_create_dt, 'YYYY MM DD') order by DT desc;


select * from r$u003_ticketlines;



select * from ffba_cashreg_log where id >= 51546 and identity='eltapos_001' order by create_dt desc;
select count(*) from ffba_cashreg_log where identity='eltapos_001';
delete from ffba_cashreg_log where identity='eltapos_001' and id < 51546;


select * from ffba_cashreg_log where id >= 51547 and identity='eltapos_002' order by create_dt desc;
select count(*) from ffba_cashreg_log where identity='eltapos_002';
delete from ffba_cashreg_log where identity='eltapos_002' and id < 51547;


select * from ffba_cashreg_log where id >= 51548 and identity='eltapos_003' order by create_dt desc;
select count(*) from ffba_cashreg_log where identity='eltapos_003';
delete from ffba_cashreg_log where identity='eltapos_003' and id < 51548;


select * from ffba_cashreg_log order by create_dt desc;


select * from ffba_cashreg_log where identity='eltapos_002' and level_name = 'ERROR' order by create_dt desc;

select identity, count(*) from ffba_cashreg_log group by identity;

delete from ffba_cashreg_log where identity='eltapos_001' and id <= 26712;
delete from ffba_cashreg_log where identity='eltapos_002' and id <= 20274;


delete from ffba_cashreg_log where identity='eltapos_002';
delete from ffba_cashreg_log where create_dt <= '2017-09-03 23:59:59';



CREATE TABLE ffba_cashreg_repl_table (id serial NOT NULL, table_name character varying(63) NOT NULL, last_repl_id bigint NOT NULL, last_update_dt timestamp with time zone, cashreg_id integer NOT NULL);

DELETE FROM ffba_cashreg_repl_table r WHERE r.cashreg_id = 4 AND r.table_name = 'draweropened';

grant select on ffba_cashreg_action to ffba_cashreg_role;
grant select, update on ffba_cashreg_action_exec to ffba_cashreg_role;
grant select on pg_authid to ffba_cashreg_role;
GRANT USAGE, SELECT ON SEQUENCE ffba_cashreg_repl_table_id_seq TO ffba_cashreg_role;

grant select, insert, update, delete on ffba_cashreg_repl_table to ffba_cashreg_role;


revoke select, insert, update on ffba_cashreg_action from ffba_cashreg_role;
revoke select, update on ffba_cashreg_action_exec from ffba_cashreg_role;



grant select, insert, update on ffba_cashreg_module_deploy to ffba_cashreg_role;
grant execute on FUNCTION ffba_cashreg_get_config(integer) to ffba_cashreg_role;
grant select on ffba_cashreg_config to ffba_cashreg_role;


select * from ffba_cashreg_module;
insert into ffba_cashreg_module (create_dt, name, content, status, create_user_id, root) values (now(), 'tittles.py', '', 'A', 2, false);

select * from ffba_cash_record where id >= 1262;
update ffba_cash_record set create_user_id = 12 where id >= 1262;


CREATE TABLE ffba_cashreg_config (id serial NOT NULL, create_dt timestamp with time zone NOT NULL, modify_dt timestamp with time zone, db_user_current character varying(100) NOT NULL, db_pass_current character varying(100) NOT NULL, db_name_current character varying(100) NOT NULL, db_host_current character varying(100) NOT NULL, cashreg_id integer NOT NULL, create_user_id integer NOT NULL, modify_user_id integer);
CREATE TABLE ffba_cashreg_config_history (id integer NOT NULL, create_dt timestamp with time zone NOT NULL, modify_dt timestamp with time zone, db_user_current character varying(100) NOT NULL, db_pass_current character varying(100) NOT NULL, db_name_current character varying(100) NOT NULL, db_host_current character varying(100) NOT NULL, history_id serial NOT NULL, history_date timestamp with time zone NOT NULL, history_type character varying(1) NOT NULL, cashreg_id integer, create_user_id integer, history_user_id integer, modify_user_id integer);

alter table ffba_cashreg_config set (db_name_current null, db_host_current is null);

ALTER TABLE ffba_cashreg_config_history ALTER COLUMN db_name_current DROP NOT NULL;
ALTER TABLE ffba_cashreg_config_history ALTER COLUMN db_host_current DROP NOT NULL;

CREATE OR REPLACE FUNCTION ffba_cashreg_get_config(_cashreg_id integer)
  RETURNS TABLE (
    db_user_current varchar,
    db_pass_current varchar,
    db_name_current varchar,
    db_host_current varchar)
  AS $func$
BEGIN
  RETURN QUERY
  SELECT c.db_user_current,
         c.db_pass_current,
         c.db_name_current,
         c.db_host_current
    FROM ffba_cashreg_config c
   WHERE c.cashreg_id = 4;
END
$func$ LANGUAGE plpgsql;

select * from ffba_cashreg_get_config(4);


create table "#test" (id integer);

insert into "#test" values (5);

select * from "#test";


SELECT n.nspname, c.relname,
  CASE c.relkind WHEN 'r' THEN 'table' WHEN 'v' THEN 'view' WHEN 'm' THEN 'materialized view' WHEN 'i' THEN 'index' WHEN 'S' THEN 'sequence' WHEN 's' THEN 'special' WHEN 'f' THEN 'f
oreign table' END,
  u.usename
  FROM pg_catalog.pg_user u, pg_catalog.pg_namespace n, pg_catalog.pg_class c
 WHERE n.oid = c.relnamespace
   AND u.usesysid = c.relowner
   AND n.nspname <> 'pg_catalog'
   AND n.nspname <> 'information_schema'
   AND n.nspname !~ '^pg_toast'
   AND pg_catalog.pg_table_is_visible(c.oid)
;

pg_catalog.pg_user u on (c.relowner = u.usesysid);


select count(*) from r$u003_tickets;


select to_char(r$_create_dt, 'YYYY MM DD') DT, count(*), sum(price*units) from r$u003_ticketlines group by to_char(r$_create_dt, 'YYYY MM DD') order by DT desc;
select to_char(r$_create_dt, 'YYYY MM DD') DT, count(*), sum(price*units) from r$u004_ticketlines group by to_char(r$_create_dt, 'YYYY MM DD') order by DT desc;
select to_char(r$_create_dt, 'YYYY MM DD') DT, count(*), sum(price*units) from r$u005_ticketlines group by to_char(r$_create_dt, 'YYYY MM DD') order by DT desc;

select dt, sum(cnt) cnt, to_char(sum(amnt), '999,999,999D09') amnt from
  (select to_char(r$_create_dt, 'YYYY MM DD') DT, count(*) cnt, sum(price*units) amnt from r$u003_ticketlines group by dt
   union select to_char(r$_create_dt, 'YYYY MM DD') DT, count(*), sum(price*units) from r$u004_ticketlines group by dt
   union select to_char(r$_create_dt, 'YYYY MM DD') DT, count(*), sum(price*units) from r$u005_ticketlines group by dt) s
group by dt
order by DT desc;


select * from r$u003_ticketlines;
