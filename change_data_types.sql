--Changes data types to correct formatting in 'orders_table' table.
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ALTER TABLE orders_table
    ALTER COLUMN date_uuid SET DATA TYPE UUID USING (uuid_generate_v4());

ALTER TABLE orders_table 
    ALTER COLUMN user_uuid SET DATA TYPE UUID USING (uuid_generate_v4());

ALTER TABLE orders_table
    ALTER COLUMN card_number TYPE VARCHAR(19);

ALTER TABLE orders_table
    ALTER COLUMN store_code TYPE VARCHAR(12);

ALTER TABLE orders_table
    ALTER COLUMN product_code TYPE VARCHAR(11);

ALTER TABLE orders_table
    ALTER COLUMN product_quantity TYPE SMALLINT;


--Changes data types to correct formatting in 'dim_users' table.

ALTER TABLE dim_users
    ALTER COLUMN first_name TYPE VARCHAR(255);

ALTER TABLE dim_users
    ALTER COLUMN last_name TYPE VARCHAR(255);

ALTER TABLE dim_users
    ALTER COLUMN date_of_birth TYPE DATE;

ALTER TABLE dim_users
    ALTER COLUMN country_code TYPE VARCHAR(3);

ALTER TABLE dim_users
    ALTER COLUMN user_uuid TYPE UUID USING (uuid_generate_v4());

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
    ALTER COLUMN staff_numbers TYPE integer USING (trim(staff_numbers)::integer);

ALTER TABLE dim_store_details
    ALTER COLUMN opening_date TYPE DATE;

ALTER TABLE dim_store_details
    ALTER COLUMN store_type TYPE VARCHAR(255);

ALTER TABLE dim_store_details
    ALTER COLUMN latitude TYPE FLOAT;

ALTER TABLE dim_store_details
    ALTER COLUMN country_code TYPE VARCHAR(2);

ALTER TABLE dim_store_details
    ALTER COLUMN continent TYPE VARCHAR(255);
