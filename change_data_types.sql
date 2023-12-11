ALTER TABLE order_details
    ALTER COLUMN date_uuid TYPE UUID;
ALTER TABLE order_details
    ALTER COLUMN user_uuid TYPE UUID;
ALTER TABLE order_details
    ALTER COLUMN card_number TYPE VARCHAR(19);
ALTER TABLE order_details
    ALTER COLUMN store_code TYPE VARCHAR(12);
ALTER TABLE order_details
    ALTER COLUMN product_code TYPE VARCHAR(11);
ALTER TABLE order_details
    ALTER COLUMN product_quantity TYPE SMALLINT;

ALTER TABLE dim_users
    ALTER COLUMN first_name TYPE VARCHAR(255);
ALTER TABLE dim_users
    ALTER COLUMN last_name TYPE VARCHAR(255);
ALTER TABLE dim_users
    ALTER COLUMN date_of_birth TYPE DATE;
ALTER TABLE dim_users
    ALTER COLUMN country_code TYPE VARCHAR(2);
ALTER TABLE dim_users
    ALTER COLUMN user_uuid TYPE UUID;

