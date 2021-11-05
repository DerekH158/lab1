import os
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker


host = os.environ["HOST"]
port = os.environ["PORT"]
user = os.environ["USER"]
password = os.environ["PASSWORD"]
db = os.environ["DW"]
dbtype = "postgresql+psycopg2"

SQLALCHEMY_DATABASE_URL = f"{dbtype}://{user}:{password}@{host}:{port}/{db}"

dwEngine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping = True)
dwSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=dwEngine)
