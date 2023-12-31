--Changes data types to correct formatting in 'orders_table' table.

ALTER TABLE orders_table
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;


ALTER TABLE orders_table
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;


ALTER TABLE orders_table
ALTER COLUMN card_number TYPE VARCHAR(25);


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
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;


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

--Alterations to the dim_products table.

UPDATE dim_products
SET product_price = REPLACE(product_price,'£','')::FLOAT;

ALTER TABLE dim_products
ALTER COLUMN product_price TYPE numeric USING (product_price::numeric);


ALTER TABLE dim_products ADD COLUMN weight_class VARCHAR(50);


ALTER TABLE dim_products RENAME COLUMN removed TO still_available;


ALTER TABLE dim_products
ALTER COLUMN weight TYPE double precision USING (trim(weight)::double precision);


ALTER TABLE dim_products
ALTER COLUMN EAN TYPE VARCHAR(255);


ALTER TABLE dim_products
ALTER COLUMN product_code TYPE VARCHAR(255);


ALTER TABLE dim_products
ALTER COLUMN date_added TYPE DATE;


ALTER TABLE dim_products
ALTER COLUMN uuid TYPE UUID USING uuid::UUID;


ALTER TABLE dim_products
ALTER COLUMN weight_class TYPE VARCHAR(255);


UPDATE dim_products
SET still_available = REPLACE(still_available,'Still_avaliable','True');


UPDATE dim_products
SET still_available = REPLACE(still_available,'Removed','False');


ALTER TABLE dim_products
ALTER COLUMN still_available TYPE BOOLEAN USING (still_available::BOOLEAN);


UPDATE dim_products
SET weight_class = CASE
                       WHEN weight < 10 THEN 'Light'
                       WHEN weight >= 10
                            AND weight < 50 THEN 'Medium'
                       WHEN weight >= 50 THEN 'Heavy'
                   END;


ALTER TABLE dim_date_times
ALTER COLUMN month TYPE VARCHAR(100);


ALTER TABLE dim_date_times
ALTER COLUMN year TYPE VARCHAR(100);


ALTER TABLE dim_date_times
ALTER COLUMN day TYPE VARCHAR (100);


ALTER TABLE dim_date_times
ALTER COLUMN time_period TYPE VARCHAR(100);


ALTER TABLE dim_date_times
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;


ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE VARCHAR(25);


ALTER TABLE dim_card_details
ALTER COLUMN expiry_date TYPE VARCHAR(5);


ALTER TABLE dim_card_details
ALTER COLUMN date_payment_confirmed TYPE DATE USING date_payment_confirmed::date;