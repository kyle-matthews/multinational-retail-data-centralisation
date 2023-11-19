from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
connector = DatabaseConnector()
extractor = DataExtractor()
cleaner = DataCleaning()

connector.list_db_tables()

table_name = 'legacy_users'
df = extractor.read_rds_table(connector, table_name)
#print(legacy_users)

clean_df = cleaner.clean_user_data(df)


connector.upload_to_db(clean_df, 'dim_users')

#payment_data = extractor.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')

#print(payment_data)