import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL', "postgresql://postgres:password@localhost:5432/portfolio_db")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autoflush= False, autocommit= False, bind= engine)

Base = declarative_base()




