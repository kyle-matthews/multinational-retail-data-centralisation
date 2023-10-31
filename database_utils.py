import yaml
import sqlalchemy

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
        The function `init_db_engine` initializes a database engine using the credentials read from a
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