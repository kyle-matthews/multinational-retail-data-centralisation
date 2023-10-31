import pandas
from database_utils import DatabaseConnector

class DataExtractor:
    def read_rds_table(self, DatabaseConnector, table_name):
        list_db_tables(self)