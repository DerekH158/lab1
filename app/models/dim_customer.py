from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import column_property
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, Numeric

Base = declarative_base()
class customer(Base):
    __table_args__ = {"schema":"group1"}  ##
    __tablename__='dim_customer'
    sk_customer=Column(Integer, primary_key = True)
    firstname=Column(String(50))
    lastname=Column(String(50))
    Name = column_property(firstname + " " + lastname)


    def __repr__(self):
        return f'{self.sk_customer} {self.firstname} {self.lastname} {self.Name}'


 

