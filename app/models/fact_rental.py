from sqlalchemy.sql.sqltypes import SMALLINT, DateTime
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
    date = relationship("group1.dim_date", back_populates = "group1.dm_customer")


    #def __repr__(self):
        #return f'{self.sk_customer} {self.firstname} {self.lastname} {self.Name}'


class Date(Base):
    __table_args__ = {"schema":"group1"}  ##
    __tablename__='dim_date'
    sk_date = Column(DateTime, primary_key=True)
    quarter = Column(DateTime,nullable=True)
    year = Column(DateTime,nullable=True)
    Month = Column(DateTime,nullable=True)
    day = Column(DateTime,nullable=True)
    sk_customer=Column(SMALLINT, ForeignKey("group1.dm_customer.id"))
    customer = relationship("group1.dim_customer", back_populates = "group1.dim_date")

     
    def __repr__(self):
        return f'{self.sk_date} {self.quarter} {self.year} {self.Month} {self.day}'


class Store(Base):
    __table_args__ = {"schema":"group1"} ##
    __tablename__='dim_store'
    sk_store=Column(Integer,primary_key = True)
    manager_staff_id = Column(VARCHAR)
    address_id = Column(SMALLINT)
    Last_update = Column(DateTime)

    def __repr__(self):
        return f'{self.sk_store} {self.manager_staff_id} {self.address_id} {self.Last_update}'

class film(Base):
    __table_args__ = {"schema":"group1"}  ##
    __tablename__='dim_film'
    sk_film=Column(Integer, primary_key = True)
    rating_code = Column(Numeric(precision=5, scale=2))
    film_duration = Column(SMALLINT)
    rental_duration = Column(SMALLINT)
    language = Column(String(50))  
    title = Column(VARCHAR(length=50))
    
    
    def __repr__(self):
        return f'{self.sk_film} {self.rating_code} {self.film_duration} {self.rental_duration} {self.language} {self.last_update} {self.title}'


class staff(Base):
    __table_args__ = {"schema":"group1"} ##
    __tablename__='dim_staff'
    staff_id=Column(Integer, primary_key = True)
    firstname=Column(String(50))
    lastname=Column(String(50))
    #Name = column_property(firstname + " " + lastname)
    email = Column(VARCHAR(length=50))

    def __repr__(self):
        return f'{self.staff_id} {self.firstname} {self.lastname} {self.email}'
