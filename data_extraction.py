import pandas as pd
from database_utils import DatabaseConnector
from sqlalchemy import create_engine
import tabula
import requests

"""The `DataExtractor` class provides methods for reading data from an RDS table and uploading data to
a database table."""
class DataExtractor:

        def read_rds_table(self, db_connector, table_name):
            """
            The function reads a table from a database using a database connector and returns the data as a
            pandas DataFrame.
            
            :param db_connector: The `db_connector` parameter is an object that is responsible for connecting to
            the database and initializing the database engine. It likely has methods such as `init_db_engine`
            that takes a YAML file containing the database credentials and returns an engine object
            :param table_name: The `table_name` parameter is a string that represents the name of the table in
            the database that you want to read
            :return: a pandas DataFrame object.
            """
            engine = db_connector.init_db_engine('db_creds.yaml')
            df = pd.read_sql_table(table_name, engine)
            return df
        
        def retrieve_pdf_data(self, link):
            """
            The function retrieves data from a PDF file using the tabula library and returns it as a DataFrame.
            
            :param link: The `link` parameter is the URL or file path of the PDF file that you want to retrieve
            data from
            :return: the variable "payment_data_df", which is a DataFrame containing the payment data extracted
            from the PDF file.
            """
            payment_data = tabula.read_pdf(link, pages='all')
            payment_data_df = payment_data[0]
            return payment_data_df
        
        def __init__(self):
            self.header = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}

        def list_number_of_stores(self, number_stores_endpoint):
            """
            The function "list_number_of_stores" makes a GET request to a specified endpoint and returns the
            number of stores.
            
            :param number_stores_endpoint: The `number_stores_endpoint` parameter is the URL endpoint that you
            want to send a GET request to in order to retrieve the number of stores
            :return: the response object from the GET request made to the `number_stores_endpoint`.
            """
            store_number = requests.get(number_stores_endpoint, params=None, headers = self.header)
            return store_number
        
        def retrieve_stores_data(self, retrieve_store_endpoint):
            store_data = requests.get(retrieve_store_endpoint, params=None, headers=self.header)
            
            stores_data_list = []
            for store_number in range(1, self.store_number) + 1:
                store_endpoint = retrieve_store_endpoint.format(store_number=store_number)
                store_data = self.retrieve_stores_data(store_endpoint)
                stores_data_list.append(store_data)
            return store_data