from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://postgres:12345@localhost:5432/project6"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
