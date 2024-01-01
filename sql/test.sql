ALTER TABLE dim_products
ALTER COLUMN product_price TYPE double precision USING (trim(product_price)::double precision);