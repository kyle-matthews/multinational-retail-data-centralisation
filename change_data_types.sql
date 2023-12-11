--Changes data types to correct formatting in 'order_details' table.
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

--Changes data types to correct formatting in 'dim_users' table.
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
ALTER TABLE dim_users
    ALTER COLUMN join_date TYPE DATE;

--This should update the data types in the dim_store_details table. (Should.)
ALTER TABLE dim_store_details
    ALTER COLUMN longitude TYPE FLOAT;
ALTER TABLE dim_store_details
    ALTER COLUMN locality TYPE VARCHAR(255);
ALTER TABLE dim_store_details
    ALTER COLUMN store_code TYPE VARCHAR(12);
ALTER TABLE dim_store_details
    ALTER COLUMN staff_numbers TYPE SMALLINT;
ALTER TABLE dim_store_details
    ALTER COLUMN opening_date TYPE DATE;
ALTER TABLE dim_store_details
    ALTER COLUMN store_type TYPE VARCHAR(255) NULLABLE;
ALTER TABLE dim_store_details
    ALTER COLUMN latitude TYPE FLOAT;
ALTER TABLE dim_store_details
    ALTER COLUMN country_code TYPE VARCHAR(2);
ALTER TABLE dim_store_details
    ALTER COLUMN continent TYPE VARCHAR(255);
