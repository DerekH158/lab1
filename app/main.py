import datetime as dt
import logging
import pandas as pd 
import models.fact_rental as models ####
from datetime import datetime
from sqlalchemy.sql.expression import column
from database.dw_session import dwEngine
from database.oltp_session import oltpEngine
from sqlalchemy.schema import CreateSchema


logging.basicConfig(level=logging.INFO,filename ="debug.logs")
logger = logging.getLogger(__name__)


def setup(engine, schema_name):

    
    if not engine.dialect.has_schema(engine, schema_name):
        engine.execute(CreateSchema(schema_name))


models.Base.metadata.create_all(bind="engine", checkfirst=True)


def extract(table_name, engine):

    df = pd.read_sql_table(table_name, con=engine.connect())
    return df

def customer_transform(df):
    df1 = df[['sk_customer', 'firstname', 'lastname']]
    df1['Name'] = df1['firstname'] + df1['lastname']
    return df1


def date_transform(df):
    df1 = df[['sk_date','quarter','year','month','day']]
    df1['sk_date'] = pd.to_datetime(df1['sk_date'], format="%d%m%Y%H")
    df1['quarter'] = df1['sk_date'].dt.quarter
    df1['Year'] = pd.to_datetime(df1['sk_date']).year
    df1['Month'] = pd.to_datetime(df1['sk_date']).month
    df1['Day'] =  pd.to_datetime(df1['sk_date']).day

    
    
def staff_transform(df):
    df1 = df[['sk_store', 'manager_staff_id','address_id','last_update']]
    return df1

def film_transform(df):
    df1 = df[['sk_film','rating_code','file_duration','rental_duration','language','title']]
    return df1

def staff_transform(df):
    df1 = df[['staff_id','firstname','lastname', 'email']]
    df1['Name'] = df1['firstname'] + df1['lastname']
    return df1


def count_rentals(df):
    df1 = df.groupby('sk_date').count()
    return df1


def loading(df, connect, postgresql_table = 'group1'):
     connect.close()
    engine.dispose()

       
############################## remining this part
#if __name__ == '__main__':
 #   try:
  #      con=engine.connect()
  #      print ("connected to database")
  #  except :
#     print("database not connected")
   #     models.Base.metadata.create_all(engine)
   #     exit(); 
        conn.close()
        engine.dispose()

exit();



































if __name__ =='__main__':
    Base.metadata.create_all(engine)