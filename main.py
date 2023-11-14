from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
connector = DatabaseConnector()
extractor = DataExtractor()
cleaner = DataCleaning()
#print(connector.read_db_creds())

#connector.list_db_tables()



table_name_2 = 'legacy_users'
legacy_users = extractor.read_rds_table(connector, table_name_2)

cleaned_data = cleaner.clean_user_data(legacy_users)

print(cleaned_data)