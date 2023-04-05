from sqlalchemy import create_engine
import os

class Connection:
    def __init__(self, port_override="5440"):

        connection_str = "postgresql+psycopg2://postgres:postgrespw@localhost:5440/postgres"

        if os.environ.get('IS_DOCKER', False):
            connection_str = "postgresql+psycopg2://postgres:postgrespw@:%s/postgres" % port_override

        self.engine = create_engine(connection_str, echo=False)
