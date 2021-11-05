import os
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker


host = os.environ["HOST"]
port = os.environ["PORT"]
user = os.environ["USER"]
password = os.environ["PASSWORD"]
db = os.environ["OLTP"]
dbtype = "postgresql+psycopg2"

SQLALCHEMY_DATABASE_URL = f"{dbtype}://{user}:{password}@{host}:{port}/{db}"

oltpEngine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping = True)
oltpSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=oltpEngine)