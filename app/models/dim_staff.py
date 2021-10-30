from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import column_property
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, Numeric

Base = declarative_base()
class staff(Base):
    __table_args__ = {"schema":"group1"} ##
    __tablename__='dim_staff'
    staff_id=Column(Integer, primary_key = True)
    firstname=Column(String(50))
    lastname=Column(String(50))
    Name = column_property(firstname + " " + lastname)
    email = Column(VARCHAR(length=50))
    #store_id = Column(SMALLINT)


    def __repr__(self):
        return f'{self.staff_id} {self.firstname} {self.lastname} {self.Name} {self.email}'
