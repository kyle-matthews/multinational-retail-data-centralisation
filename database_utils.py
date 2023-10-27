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


        return 
