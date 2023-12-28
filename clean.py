import pandas as pd

class DataExtractor:
    def read_rds_table(self, db_connector, table_name):
        engine = db_connector.init_db_engine()
        df = pd.read_sql_table(table_name, engine)
        df_clean = self.clean_data(df)
        return df_clean
    
    def clean_data(self, df):
        df_clean = df.dropna()
        return df_clean