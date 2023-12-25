from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from databases import Database

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

database = Database(DATABASE_URL)
metadata.create_all(engine)
