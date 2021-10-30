from datetime import date
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import column_property
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, VARCHAR, Numeric,SMALLINT,VARCHAR
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()
class film(Base):
    __table_args__ = {"schema":"group1"}  ##
    __tablename__='dim_film'
    sk_film=Column(Integer, primary_key = True)
    rating_code = Column(Numeric(precision=5, scale=2))
    film_duration = Column(SMALLINT)
    rental_duration = Column(SMALLINT)
    language = Column(String(50))  ###
    last_update = Column((DateTime)) 
    title = Column(VARCHAR(length=50))
    
    
    def __repr__(self):
        return f'{self.id} {self.rating_code} {self.film_duration} {self.rental_duration} {self.language} {self.last_update} {self.title}'

