from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import pandas as pd
import numpy as np
import yaml
import sqlalchemy
import psycopg2

if __name__ == "__main__":
    # Create instances of your classes
    db_connector = DatabaseConnector()
    data_extractor = DataExtractor()
    data_cleaner = DataCleaning()

    # Extract data from the RDS database
    table_name = 'your_user_data_table'
    user_data = data_extractor.read_rds_table(db_connector, table_name)

    # Clean the user data
    cleaned_data = data_cleaner.clean_user_data(user_data)

    # Upload cleaned data to the database
    db_connector.upload_to_db(cleaned_data, 'dim_users')