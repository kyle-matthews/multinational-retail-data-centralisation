--Changes data types to correct formatting in 'orders_table' table.
/*CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE orders_table
    ALTER COLUMN date_uuid SET DATA TYPE UUID USING (uuid_generate_v4()),
    ALTER COLUMN user_uuid SET DATA TYPE UUID USING (uuid_generate_v4()),
    ALTER COLUMN card_number TYPE VARCHAR(19),
    ALTER COLUMN store_code TYPE VARCHAR(12),
    ALTER COLUMN product_code TYPE VARCHAR(11),
    ALTER COLUMN product_quantity TYPE SMALLINT;


--Changes data types to correct formatting in 'dim_users' table.

ALTER TABLE dim_users
    ALTER COLUMN first_name TYPE VARCHAR(255),
    ALTER COLUMN last_name TYPE VARCHAR(255),
    ALTER COLUMN date_of_birth TYPE DATE,
    ALTER COLUMN country_code TYPE VARCHAR(3),
    ALTER COLUMN user_uuid TYPE UUID USING (uuid_generate_v4()),
    ALTER COLUMN join_date TYPE DATE;

--This should update the data types in the dim_store_details table. (Should.)
ALTER TABLE dim_store_details
    ALTER COLUMN longitude TYPE FLOAT,
    ALTER COLUMN locality TYPE VARCHAR(255),
    ALTER COLUMN store_code TYPE VARCHAR(12),
    ALTER COLUMN staff_numbers TYPE integer USING (trim(staff_numbers)::integer),
    ALTER COLUMN opening_date TYPE DATE,
    ALTER COLUMN store_type TYPE VARCHAR(255),
    ALTER COLUMN latitude TYPE FLOAT,
    ALTER COLUMN country_code TYPE VARCHAR(2),
    ALTER COLUMN continent TYPE VARCHAR(255);*/

--Alterations to the dim_products table. 
UPDATE dim_products
    SET product_price = REPLACE(
        product_price,
        '£',
        ''
        )::FLOAT;
ALTER TABLE dim_products
    ADD COLUMN weight_class VARCHAR(50);

ALTER TABLE dim_products
    RENAME COLUMN removed TO still_available;


ALTER TABLE dim_products
    ALTER COLUMN weight TYPE FLOAT,
    ALTER COLUMN EAN TYPE VARCHAR(255),
    ALTER COLUMN product_code TYPE VARCHAR(255),
    ALTER COLUMN date_added TYPE DATE,
    ALTER COLUMN uuid TYPE UUID,
    ALTER COLUMN still_available TYPE BOOL,
    ALTER COLUMN weight_class TYPE VARCHAR(255);

UPDATE dim_products
    SET weight_class = 
        CASE
            WHEN weight < 10 THEN 'Light'
            WHEN weight >= 10 AND weight < 50 THEN 'Medium'
            WHEN weight >= 50 THEN 'Heavy'
        END;


