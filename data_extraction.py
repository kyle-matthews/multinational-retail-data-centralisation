import pandas as pd
import numpy as np
from database_utils import DatabaseConnector

# The DataExtractor class has a method called upload_to_db that uploads a DataFrame to a database
# table.
class DataExtractor:
        def upload_to_db(self, df, table_name):
        DatabaseConnector.engine = self.init_db_engine()
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        