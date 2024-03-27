from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

src_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
db_path = os.path.join(src_directory, 'temp.db') 
sqlite_url = f"sqlite:///{db_path}"  # URL do banco de dados SQLite


#!#########################    SQLITE   ############################
Base = declarative_base()


engine = create_engine(sqlite_url)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
