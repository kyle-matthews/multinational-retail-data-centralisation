--Primary Key assignment, following code has been pushed. Postgresql will think you're trying to assign two primary keys if you re-run the query.

ALTER TABLE dim_users ADD PRIMARY KEY(user_uuid);


ALTER TABLE dim_store_details ADD PRIMARY KEY(store_code);


ALTER TABLE dim_products ADD PRIMARY KEY(product_code);


ALTER TABLE dim_date_times ADD PRIMARY KEY(date_uuid);


ALTER TABLE dim_card_details ADD PRIMARY KEY(card_number);

-- Adds unique constraint to user_uuid before creating foreign key.

ALTER TABLE orders_table ADD CONSTRAINT fk_user_uuid
FOREIGN KEY (user_uuid) REFERENCES dim_users(user_uuid);


ALTER TABLE orders_table ADD CONSTRAINT fk_date_uuid
FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid);


ALTER TABLE orders_table ADD CONSTRAINT fk_card_number
FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);


ALTER TABLE orders_table ADD CONSTRAINT fk_store_code
FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code);


ALTER TABLE orders_table ADD CONSTRAINT fk_product_code
FOREIGN KEY (product_code) REFERENCES dim_products(product_code);