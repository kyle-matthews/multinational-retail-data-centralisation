import pandas as pd
from database_utils import DatabaseConnector
from sqlalchemy import create_engine

"""The `DataExtractor` class provides methods for reading data from an RDS table and uploading data to
a database table."""
class DataExtractor:
        def read_rds_table(self, db_connector, table_name):
            engine = db_connector.init_db_engine()
            df = pd.read_sql_table(table_name, engine)
            return df

"""# Create an instance of the DatabaseConnector class
db_connector = DatabaseConnector()

# Create an instance of the DataExtractor class
data_extractor = DataExtractor()

# Read data from the database and store it in a DataFrame
table_name = 'car_sales'
dim_users = data_extractor.read_rds_table(db_connector, table_name)

# Upload data to the database
data_extractor.upload_to_db(dim_users, table_name, db_connector)"""

