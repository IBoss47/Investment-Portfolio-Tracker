from sqlalchemy import Column, String

from app.database import Base

class Currency(Base):
    __tablename__ = 'currencies'

    currency_code = Column(String(3), primary_key= True)
    currency_name = Column(String, nullable= False)