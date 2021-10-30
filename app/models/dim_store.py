from datetime import date
from sqlalchemy.orm import declarative_base, query_expression
from sqlalchemy.orm import column_property
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, Numeric,SMALLINT, VARCHAR
from sqlalchemy.sql.expression import join
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

class Store(Base):
    __table_args__ = {"schema":"group1"} ##
    __tablename__='dim_store'

    sk_store=Column(Integer,primary_key = True)
    manager_staff_id = Column(VARCHAR)
    address_id = Column(SMALLINT, ForeignKey("group1.address.id"))
    Last_update = Column(DateTime)
    staff = relationship("group1.dim_staff", back_populates = "group1.dm_store")
    address = relationship("group1.address", back_populates ="group1.dm_store")

    
    def __repr__(self):
        return f'{self.sk_store} {self.manager_staff_id} {self.address_id} {self.Last_update}'

class Staff(Base):
    __table_args__ = {"schema":"group1"}
    __tablename__='dim_staff'

    staff_id=Column(Integer, primary_key = True)
    firstname=Column(String(50))
    lastname=Column(String(50))
    Name = column_property(firstname + " " + lastname)
    email = Column(VARCHAR(length=50))
    store_id = Column(SMALLINT, ForeignKey("group1.dim_store.id"))
    store = relationship("group1.dim_store", back_populates = "group1.dim_staff")

    def __repr__(self):
        return f'{self.staff_id} {self.firstname} {self.lastname} {self.Name} {self.email} {self. store_id}'


class address(Base):
    __table_args__ = {"schema":"group1"}
    __tablename__='address'

    address_id = Column(Integer, primary_key = True)
    address = Column(VARCHAR(length=50))
    district = Column(VARCHAR(length=50))
    city_id =Column(SMALLINT, ForeignKey("group1.city.id"))
    phone_code = Column(VARCHAR(length=50))
    phone = Column(VARCHAR(length=50))
    last_update = Column(DateTime)
    store = relationship("group1.dim_store", back_populates = "group1.address")
    city = relationship("group1.city", back_populates ="group1.address")


    def __repr__(self):
        return f'{self.address_id} {self.address} {self.district} {self.city_id} {self.phone_code} {self.last_update}'

 
class City(Base):
    __table_args__ = {"schema":"group1"}
    __tablename__='city'
    city_id = Column(Integer, primary_key = True)
    city = Column(VARCHAR(length=50))
    country_id = Column(SMALLINT,ForeignKey("group1.country.id"))
    last_update = Column(DateTime)
    address = relationship("group1.address", back_populates ="group1.city")
    country = relationship("group1.country", back_populates ="group1.city")

    def __repr__(self):
            return f'{self.city_id} {self.city} {self.country_id} {self.last_update}'

    ## NOTEEEEEE
### state will be extracted as district from the address table

class Country(Base):
    __table_args__ = {"schema":"group1"}
    __tablename__='country'
    country_id =Column (Integer, primary_key = True)
    country = Column(VARCHAR)
    last_update = Column(DateTime)
    City = relationship("group1.city", back_populates ="group1.country")

    def __repr__(self):
            return f'{self.country_id} {self.country} {self.last_update}'








# .query_expression(store, staff).join(staff).all()
#query = session.query(table_1).join(table_2, table_1.ID==table_2.ID_1).filter(table_1.ID == 11)























