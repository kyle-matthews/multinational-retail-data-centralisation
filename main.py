import pandas as pd
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
connector = DatabaseConnector()
extractor = DataExtractor()
cleaner = DataCleaning()

#creds = 'db_creds.yaml'
#df = extractor.read_rds_table(connector, 'legacy_users')

#clean_df = cleaner.clean_user_data(df)

#connector.upload_to_db(clean_df, 'dim_users')

#payment_data_df = extractor.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')
#print(payment_data_df)

#clean_payment_data = cleaner.clean_card_data(payment_data_df)

#print(clean_payment_data)

api_key = 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'
number_of_stores_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
retrieve_store_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'

# Connects to API to retrieve the number of stores.
#num_stores = extractor.list_number_of_stores(number_of_stores_endpoint)


#print("Value of num_stores:", num_stores)

# Connects to API to collect store information and passes it as a Dataframe.
#store_df = extractor.retrieve_stores_data(452)
#print(store_df.head(5))

#cleaned_store_data = cleaner.clean_store_data(store_df)
#print(cleaned_store_data)


products_df = extractor.extract_from_s3('s3://data-handling-public/products.csv')
print(products_df.head(5))

creds = 'PgAdmin.yaml'
connector.upload_to_db(products_df, 'clean_products_data')