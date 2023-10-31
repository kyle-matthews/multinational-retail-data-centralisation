import pandas
from database_utils import DatabaseConnector

class DataExtractor:
    def read_rds_table(self, DatabaseConnector, table_name):
        DatabaseConnector.list_db_tables()
        