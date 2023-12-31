--This is where queries on the sales_data database will be stored.

--Retrieves number of stores in each country. 
SELECT country_code, COUNT(country_code) AS total_no_stores
FROM dim_store_details
GROUP BY country_code;

--Queries which locations have the most stores.
SELECT locality, COUNT(*) AS total_no_stores
FROM dim_store_details
GROUP BY locality
ORDER BY total_no_stores DESC;

--Queries which months produce the most sales.
SELECT ROUND(SUM(dim_products.product_price * orders_table.product_quantity), 2) AS total_sales,
       dim_date_times.month AS month
FROM orders_table
JOIN dim_products ON orders_table.product_code = dim_products.product_code
JOIN dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
GROUP BY month
ORDER BY total_sales DESC;

--Compares online and offline sales.
SELECT COUNT(orders_table.user_uuid) AS number_of_sales,
       SUM(orders_table.product_quantity) AS product_quantity_count,
       CASE
           WHEN dim_store_details.store_type = 'Web Portal' THEN 'web'
           ELSE 'offline'
       END AS location
FROM orders_table
JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY location
ORDER BY product_quantity_count ASC

