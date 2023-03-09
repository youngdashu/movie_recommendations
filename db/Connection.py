from sqlalchemy import create_engine



class Connection:
    def __init__(self):
        self.engine = create_engine("postgresql+psycopg2://youngdashu:@localhost:5432/movies", echo=True)
