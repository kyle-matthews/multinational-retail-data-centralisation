from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
connector = DatabaseConnector()
extractor = DataExtractor()
cleaner = DataCleaning()

creds = 'db_creds.yaml'
df = extractor.read_rds_table(connector, 'legacy_users')

clean_df = cleaner.clean_user_data(df)

connector.upload_to_db(clean_df, 'dim_users')




#payment_data = extractor.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')

#print(payment_data)