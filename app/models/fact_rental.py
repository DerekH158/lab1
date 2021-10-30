#importing necessary libraries
from sqlalchemy import Column, String, Date, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
#from sqlalchemy.ext.declaraitive import declarative_base
#from sqlalchemy.orm import relationship

#create the base
Base = declarative_base()

#create class named FACT
class FACT(Base):
    #create table named FACT_RENTAL
    _tablename_ = 'FACT_RENTAL'
    
    #create fields within table
    sk_customer = Column(String(50), primary_key=True)
    sk_date = Column(Date)
    sk_store = Column(String(50))
    sk_film = Column(String(50))
    sk_staff = Column(String(50))
    count_rentals = Column(Integer)