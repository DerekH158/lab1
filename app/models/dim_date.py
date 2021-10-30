from datetime import datetime
from datetime import date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import column_property
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, Numeric,SMALLINT,VARCHAR
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


Base = declarative_base()
class Date(Base):
    __table_args__ = {"schema":"group1"}  ##
    __tablename__='dim_date'
    sk_date = Column(DateTime, primary_key=True)
    quarter = Column(DateTime,nullable=True)
    year = Column(DateTime,nullable=True)
    Month = Column(DateTime,nullable=True)
    day = Column(DateTime,nullable=True)

     
    def __repr__(self):
        return f'{self.sk_date} {self.quarter} {self.yeare} {self.Month} {self.day}'
