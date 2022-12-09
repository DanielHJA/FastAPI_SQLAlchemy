import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#DATABASE_URL = os.getenv("DB_CONN")
#print(DATABASE_URL)
engine = create_engine("sqlite:///foo.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
