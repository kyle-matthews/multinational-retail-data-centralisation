import yaml
from sqlalchemy import inspect
from sqlalchemy import create_engine
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
        """db_url = sqlalchemy.engine.url.URL(
            
            username=db_creds['RDS_USER'],
            password=db_creds['RDS_PASSWORD'],
            host=db_creds['RDS_HOST'],
            port=db_creds['RDS_PORT'],
            database=db_creds['RDS_DATABASE']

                )"""
        db_url = f"postgresql+psycopg2://{db_creds['RDS_USER']}:{db_creds['RDS_PASSWORD']}@{db_creds['RDS_HOST']}:{db_creds['RDS_PORT']}/{db_creds['RDS_DATABASE']}"
        
        engine = create_engine(db_url)
        return engine
    

    def list_db_tables(self):
# The code block you provided is defining a method called `list_db_tables` in the `DatabaseConnector`
# class. This method is responsible for connecting to the database, inspecting the tables in the
# database, and returning a list of table names.
        engine = self.init_db_engine()
        table_inspector = inspect(engine)
        tables = table_inspector.get_table_names()

        print(tables)
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

        # Connect to the database
        conn = psycopg2.connect(
            user=db_creds['RDS_USER'],
            password=db_creds['RDS_PASSWORD'],
            host=db_creds['RDS_HOST'],
            port=db_creds['RDS_PORT'],
            database=db_creds['RDS_DATABASE']
        )
        cursor = conn.cursor()

        # Prepare the SQL query
        columns = ', '.join(df.columns)
        placeholders = ', '.join(['%s' for _ in range(len(df.columns))])
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Execute the query
        cursor.executemany(insert_query, df.values.tolist())
        
        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        print(f"Data successfully uploaded to the '{table_name}' table.")
