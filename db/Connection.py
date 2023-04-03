from sqlalchemy import create_engine



class Connection:
    def __init__(self):
        self.engine = create_engine("postgresql+psycopg2://postgres:@localhost:5440/docker", echo=False)
