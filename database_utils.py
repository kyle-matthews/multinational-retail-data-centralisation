import yaml
import sqlalchemy
import psycopg2

class DatabaseConnector:
    def read_db_creds(self):
        """
        The function reads database credentials from a YAML file.
        """
        with open('db_creds.yaml', 'r') as file:
            db_credentials = yaml.safe_load(file)

        return db_credentials
    
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
        The function `list_db_tables` retrieves a list of table names from a PostgreSQL database.
        :return: a list of table names in the public schema of the database.
        """
        engine = self.init_db_engine()
        with engine.connect() as connection:
            result = connection.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
            tables = [row[0] for row in result]
        return tables

    def upload_to_db(self, df, table_name):
        """
        The `upload_to_db` function uploads a pandas DataFrame to a PostgreSQL database table.
        
        :param df: The parameter `df` is a pandas DataFrame that contains the data you want to upload to the
        database. It should have columns that match the table structure in the database
        :param table_name: The `table_name` parameter is a string that specifies the name of the table in
        the database where you want to upload the data
        """
         

        db_creds = self.read_db_creds()
        # Load credentials from YAML file
        conn = psycopg2.connect(
            host=db_creds['host'],
            database=db_creds['database'],
            user=db_creds['username'],
            password=db_creds['password'],
            port=db_creds['port'] )
            
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