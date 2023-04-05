from sqlalchemy import create_engine
import os

class Connection:
    def __init__(self):

        connection_str = "postgresql+psycopg2://postgres:postgrespw@localhost:5440/postgres"

        if os.environ.get('IS_DOCKER', False):
            connection_str = "postgresql+psycopg2://postgres:postgrespw@:5440/postgres"

        self.engine = create_engine(connection_str, echo=False)
