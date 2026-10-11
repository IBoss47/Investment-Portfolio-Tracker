import uuid6
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, Numeric, Date
from sqlalchemy.sql import func

from app.database import Base

class DailyPrice(Base):
    __tablename__ = 'daily_prices'

    daily_id = Column(
        UUID(as_uuid= True),
        primary_key= True,
        index= True,
        default= uuid6.uuid7
    )
    instrument_id = Column(
        UUID(as_uuid= True),
        nullable= False
    )

    close_price = Column(Numeric(24, 10), nullable= False)
    price_date = Column(Date, nullable= False)
    create_at = Column(DateTime(timezone= True), server_default= func.now())