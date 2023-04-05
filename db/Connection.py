import sys

from sqlalchemy import create_engine
import os

class Connection:
    def __init__(self):

        port = int(sys.argv[1]) if len(sys.argv) > 1 else 5440

        connection_str = "postgresql+psycopg2://postgres:postgrespw@localhost:5440/postgres"

        if os.environ.get('IS_DOCKER', False):
            connection_str = "postgresql+psycopg2://postgres:postgrespw@:%s/postgres" % port

        self.engine = create_engine(connection_str, echo=False)
