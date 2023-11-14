from database_utils import DatabaseConnector
from data_extraction import DataExtractor

connector = DatabaseConnector()

#print(connector.read_db_creds())

source_engine = connector.init_db_engine()

#connector.list_db_tables()

extractor = DataExtractor()

extractor.read_rds_table(source_engine, 'legacy_users')
