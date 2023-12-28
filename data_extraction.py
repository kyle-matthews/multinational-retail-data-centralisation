import pandas as pd
from database_utils import DatabaseConnector
from sqlalchemy import create_engine
import tabula
import requests
import boto3

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
        engine = db_connector.init_db_engine("db_creds.yaml")
        df = pd.read_sql_table(table_name, engine)
        print("Table read")
        return df

    def retrieve_pdf_data(self, link):
        """
        The function retrieves data from a PDF file using the tabula library and returns it as a DataFrame.

        :param link: The `link` parameter is the URL or file path of the PDF file that you want to retrieve
        data from
        :return: the variable "payment_data_df", which is a DataFrame containing the payment data extracted
        from the PDF file.
        """
        payment_data = tabula.read_pdf(link, pages="all")
        payment_data_df = pd.concat(payment_data)

        return payment_data_df

    def __init__(self):
        self.header = {"x-api-key": "yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}

    def list_number_of_stores(self, number_stores_endpoint):
        """
        The function "list_number_of_stores" makes a GET request to a specified endpoint and returns the
        number of stores.

        :param number_stores_endpoint: The `number_stores_endpoint` parameter is the URL endpoint that you
        want to send a GET request to in order to retrieve the number of stores
        :return: the response object from the GET request made to the `number_stores_endpoint`.
        """
        num_stores = requests.get(
            number_stores_endpoint, params=None, headers=self.header
        )
        num_stores = num_stores.text
        num_stores = int((num_stores[-4:-1]))
        return num_stores

    def retrieve_stores_data(self, num_stores: int):
        all_stores_data = []

        for store_number in range(num_stores):
            store_endpoint = f"https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}"
            response = requests.get(store_endpoint, headers=self.header)
            print(store_number)
            store_data = response.json()
            all_stores_data.append(store_data)

        store_data_df = pd.DataFrame(
            [store for store in all_stores_data if isinstance(store, dict)]
        )
        return store_data_df

    def extract_csv_from_s3(self, url):
        s3 = boto3.client("s3")
        s3.download_file(
            "data-handling-public",
            "products.csv",
            "/Users/kylematthews/Documents/AICore/multinational-retail-data-centralisation/multinational-retail-data-centralisation/products.csv",
        )
        df = pd.read_csv("products.csv")
        return df

    def extract_json_from_s3(self):
        s3 = boto3.client("s3")
        s3.download_file(
            "data-handling-public",
            "date_details.json",
            "/Users/kylematthews/Documents/AICore/multinational-retail-data-centralisation/multinational-retail-data-centralisation/date_details.json",
        )
        df = pd.read_json("date_details.json")
        return df
