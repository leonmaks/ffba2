CREATE OR REPLACE FUNCTION ffba_cash_record_set_record_date() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.record_date IS NULL THEN
        NEW.record_date := NEW.entry_date;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql
;


DROP TRIGGER ffba_cash_record_set_record_date ON ffba_cash_record;


CREATE TRIGGER ffba_cash_record_set_record_date BEFORE INSERT OR UPDATE ON ffba_cash_record
    FOR EACH ROW EXECUTE PROCEDURE ffba_cash_record_set_record_date()
;
