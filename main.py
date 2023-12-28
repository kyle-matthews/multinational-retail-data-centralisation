import pandas as pd
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

connector = DatabaseConnector()
extractor = DataExtractor()
cleaner = DataCleaning()

# Extracts, cleans and uploads user data into 'dim_users'.
creds = "db_creds.yaml"
legacy_users_df = extractor.read_rds_table(connector, "legacy_users")
legacy_users_df.to_csv("extracted_users_data.csv")
clean_df = cleaner.clean_user_data(legacy_users_df)
clean_df.to_csv("clean_users_data.csv")
connector.upload_to_db(clean_df, "dim_users")
print("Uploaded dim_users")

# Extracts, cleans and uploads payment data into 'dim_card_details'.
# payment_data_df = extractor.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')
# print(payment_data_df)
# payment_data_df.to_csv('extracted_payment_data.csv')
payment_data_df = pd.read_csv("extracted_payment_data.csv")
clean_payment_data = cleaner.clean_card_data(payment_data_df)
clean_payment_data.to_csv("clean_payment_data.csv")

connector.upload_to_db(clean_payment_data, "dim_card_details")
print("uploaded dim_card_details")

# Retrieves the number of stores from an API and then uses that information to retrieve accurate store data before cleaning and uploading to dim_store_data.
print(" The next step might take some time... Please be patient.")

# print(clean_payment_data) -- Used for debugging.

api_key = "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"
number_of_stores_endpoint = (
    "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
)
retrieve_store_endpoint = "https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}"

# Connects to API to retrieve the number of stores.
num_stores = extractor.list_number_of_stores(number_of_stores_endpoint)

# print("Value of num_stores:", num_stores) -- Used for debugging.

# Connects to API to collect store information and passes it as a Dataframe.
store_data_df = extractor.retrieve_stores_data(452)
# print(store_df.head(5))"""

store_data_df = pd.read_csv("extracted_store_data.csv")
cleaned_store_data_df = cleaner.clean_store_data(store_data_df)
cleaned_store_data_df.to_csv("clean_store_data.csv")
connector.upload_to_db(cleaned_store_data_df, "dim_store_details")
print("uploaded store details")

# Retrieves product information from an AWS s3 bucket.
products_df = extractor.extract_csv_from_s3("s3://data-handling-public/products.csv")
clean_products_df = cleaner.clean_product_weights(products_df)

creds = "PgAdmin.yaml"
connector.upload_to_db(clean_products_df, "dim_products")
print("uploaded dim_products")

# The following script performs the following tasks:
# Initiates a database engine, lists the tables in the database and prints out the names of the tables.
creds = "PgAdmin.yaml"
connector.init_db_engine(creds)
table_list = connector.list_db_tables()
print(table_list)
# Reads the 'orders_table' table from the remote database
orders_df = extractor.read_rds_table(connector, "orders_table")
orders_df.to_csv("extracted_orders.csv")
# Cleans the data using the clean_orders_data method in the 'cleaner' class.
clean_orders_df = cleaner.clean_orders_data(orders_df)
clean_orders_df.to_csv("clean_orders.csv")

# Updates creds variable to access postgres database and uploads cleaned data to central database.
creds = "PgAdmin.yaml"
connector.upload_to_db(clean_orders_df, "orders_table")
print("uploaded orders_table")

dim_date_times = extractor.extract_json_from_s3()
print("extracted")
dim_date_times.to_csv("extracted_date_times.csv")
print("csv'd")
clean_date_times = cleaner.clean_date_times(dim_date_times)
print("cleaned")
clean_date_times.to_csv("clean_date.csv")
print("clean_csv'd")


# Updates creds variable to access postgres database and uploads cleaned data to central database.
creds = "PgAdmin.yaml"
connector.upload_to_db(clean_date_times, "dim_date_times")
print("Successfully uploaded dim_date_times")