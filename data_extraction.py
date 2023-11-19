import pandas as pd
from database_utils import DatabaseConnector
from sqlalchemy import create_engine
import tabula

"""The `DataExtractor` class provides methods for reading data from an RDS table and uploading data to
a database table."""
class DataExtractor:
        def read_rds_table(self, db_connector, table_name):
            engine = db_connector.init_db_engine()
            df = pd.read_sql_table(table_name, engine)
            return df
        
        def retrieve_pdf_data(self, link):
              payment_data = tabula.read_pdf(link, pages='all')
              return payment_data