import pandas as pd
from database_utils import DatabaseConnector
from sqlalchemy import create_engine
import tabula
import requests

"""The `DataExtractor` class provides methods for reading data from an RDS table and uploading data to
a database table."""
class DataExtractor:
        
        header = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}

        def read_rds_table(self, db_connector, table_name):
            engine = db_connector.init_db_engine('db_creds.yaml')
            df = pd.read_sql_table(table_name, engine)
            return df
        
        def retrieve_pdf_data(self, link):
              payment_data = tabula.read_pdf(link, pages='all')
              payment_data_df = payment_data[0]
              return payment_data_df
        
        def list_number_of_stores(self, number_stores_endpoint):
            response = requests.get(number_stores_endpoint, headers=self.header)
            return response.json().get('number_of_stores')
