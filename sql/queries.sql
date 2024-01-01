--This is where queries on the sales_data database will be stored.
 --Retrieves number of stores in each country.

SELECT country_code,
       COUNT(country_code) AS total_no_stores
FROM dim_store_details
GROUP BY country_code;

--Queries which locations have the most stores.

SELECT locality,
       COUNT(*) AS total_no_stores
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
ORDER BY product_quantity_count ASC;

--Percentages of sales through different stores.
 WITH product_details AS
    (SELECT dim_store_details.store_type, dim_products.product_price, orders_table.product_quantity
     FROM orders_table
     INNER JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
     INNER JOIN dim_products ON orders_table.product_code = dim_products.product_code),
                      cte2 AS
    (SELECT store_type, ROUND(SUM(product_price * product_quantity)) AS total_sales
     FROM product_details
     GROUP BY store_type)
SELECT store_type,
       total_sales,
       ROUND(total_sales * 100 /
                 (SELECT SUM(total_sales)
                  FROM cte2)) AS percentage_total
FROM cte2
GROUP BY store_type,
         total_sales
ORDER BY percentage_total DESC;

--Finds which month in which year has the highest sales.

SELECT ROUND(SUM(dim_products.product_price * orders_table.product_quantity), 2) AS total_sales,
       dim_date_times.year AS year,
       dim_date_times.month AS month
FROM orders_table
JOIN dim_products ON orders_table.product_code = dim_products.product_code
JOIN dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
GROUP BY year,
         month
ORDER BY total_sales DESC;

--Finds the number of employees in each country.

SELECT SUM(staff_numbers) as total_staff_numbers,
       country_code
FROM dim_store_details
GROUP BY country_code
ORDER BY total_staff_numbers DESC;

-- Finds which German store sells the most.

SELECT ROUND(SUM(dim_products.product_price * orders_table.product_quantity), 2) AS total_sales,
       dim_store_details.store_type AS store_type,
       dim_store_details.country_code AS country_code
FROM orders_table
JOIN dim_products ON orders_table.product_code = dim_products.product_code
JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
WHERE country_code = 'DE'
GROUP BY store_type,
         country_code
ORDER BY total_sales ASC;