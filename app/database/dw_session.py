#importing sqlalchemy create engine library
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#creating the engine
engine = create_engine("postgres://", echo=True, future=True)


"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

host = os.environ["HOST"]
port = os.environ["PORT"]
user = os.environ["USER"]
password = os.environ["PASSWORD"]
db = os.environ["POSTGRES_OLTP"]
dbtype = "postgresql+psycopg2"

SQLALCHEMY_DATABASE_URL = f"{dbtype}://{user}:{password}@{host}:{port}/{db}"

oltpEngine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
oltpSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=oltpEngine)

"""
