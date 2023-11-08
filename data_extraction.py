import pandas as pd
import numpy as np
from database_utils import DatabaseConnector


class DataExtractor:
        def read_rds_table(self, db_connector, table_name):
            engine = db_connector.init_db_engine()
            query = f"SELECT * FROM {table_name};"
            df = pd.read_sql(query, engine)
            return df


        def upload_to_db(self, df, table_name):
            engine = self.init_db_engine()
            df.to_sql(table_name, engine, if_exists='replace', index=False)

