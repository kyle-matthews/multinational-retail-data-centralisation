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

    def read_pgadmin_creds(self):
        with open('PgAdmin.yaml', 'r') as file:
            pg_admin_creds = yaml.safe_load(file)
        return pg_admin_creds

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
        
        engine = sqlalchemy.create_engine(db_url)
        return engine
    

    def list_db_tables(self):
# The code block you provided is defining a method called `list_db_tables` in the `DatabaseConnector`
# class. This method is responsible for connecting to the database, inspecting the tables in the
# database, and returning a list of table names.
        engine = self.init_db_engine()
        table_inspector = sqlalchemy.inspect(engine)
        tables = table_inspector.get_table_names()

        print(tables)
        return tables


    def upload_to_db(self, df, table_name):

        pg_admin = self.read_pgadmin_creds()

        # Connect to the database
        conn = psycopg2.connect(host=pg_admin['HOST'],
                                dbname=pg_admin['DB_NAME'],
                                user=pg_admin['USER'],
                                password=pg_admin['PASSWORD'])
        cur = conn.cursor()

        engine = self.init_db_engine()

        df.to_sql(name=table_name, con=engine, if_exists='replace')
        print('Data successfully uploaded.')
        
