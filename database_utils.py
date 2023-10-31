import yaml
import sqlalchemy
import psycopg2

class DatabaseConnector:
    def read_db_creds(self):
        """
        The function reads database credentials from a YAML file.
        """
        with open('db_creds.yaml', 'r') as stream:
            data_loaded = yaml.safe_load(stream)

        return data_loaded
    
    #Now create a method init_db_engine which will read the credentials 
    # from the return of read_db_creds and initialise and return an sqlalchemy database engine.

    def init_db_engine(self):
        """
        The function `init_db_engine` initialises a database engine using the credentials read from a
        file.
        :return: a SQLAlchemy engine object.
        """
        db_creds = self.read_db_creds()
        db_url = sqlalchemy.engine.url.URL(
                     
            drivername=db_creds['drivername'],
            username=db_creds['username'],
            password=db_creds['password'],
            host=db_creds['host'],
            port=db_creds['port'],
            database=db_creds['database']

                )
        
        engine = sqlalchemy.create_engine(db_url)
        return engine
    

    def list_db_tables(self):
        """
        The function `list_db_tables` returns a list of table names in a database.
        :return: a list of table names in the database.
        """
        engine = self.init_db_engine()
        inspect_engine =  inspect(engine)
        table_names = inspect_engine.get_table_names()
        return table_names

    def upload_to_db(self, df, table_name):
        """
        The `upload_to_db` function uploads a pandas DataFrame to a PostgreSQL database table.
        
        :param df: The parameter `df` is a pandas DataFrame that contains the data you want to upload to the
        database. It should have columns that match the table structure in the database
        :param table_name: The `table_name` parameter is a string that specifies the name of the table in
        the database where you want to upload the data
        """
         
        conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port
        )
        cursor = conn.cursor()


        df_columns = ', '.join(df.columns)
        df_values = [tuple(row) for row in df.values]
        insert_query = f"""
        INSERT INTO {table_name} ({df_columns})
        VALUES {', '.join(['%s'] * len(df.columns))}
        """
        cursor.executemany(insert_query, df_values)
        conn.commit()

        cursor.close()
        conn.close()

        print(f"Data successfully uploaded to the '{table_name}' table.")