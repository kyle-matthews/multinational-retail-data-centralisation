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