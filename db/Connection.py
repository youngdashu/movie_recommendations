from sqlalchemy import create_engine



class Connection:
    def __init__(self):
        self.engine = create_engine("postgresql+psycopg2://postgres:postgrespw@localhost:5440/postgres", echo=False)
