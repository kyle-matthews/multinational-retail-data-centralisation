--Primary Key assignment, following code has been pushed. Postgresql will think you're trying to assign two primary keys if you re-run the query. 
 ALTER TABLE dim_users
    ADD PRIMARY KEY(user_uuid);
ALTER TABLE dim_store_details
    ADD PRIMARY KEY(store_code);
ALTER TABLE dim_products
    ADD PRIMARY KEY(product_code);
ALTER TABLE dim_date_times
    ADD PRIMARY KEY(date_uuid);
ALTER TABLE dim_card_details
    ADD PRIMARY KEY(card_number);

-- Adds unique constraint to user_uuid before creating foreign key.
ALTER TABLE orders_table
    ADD CONSTRAINT user_uuid UNIQUE (user_uuid);

--Foreign Key assignment for 'order_details'.
ALTER TABLE dim_users 
ADD CONSTRAINT ID
FOREIGN KEY (user_uuid) 
REFERENCES orders_table (user_uuid);