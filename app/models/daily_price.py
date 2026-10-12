import uuid6
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, Numeric, Date, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

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
        ForeignKey('instruments.instrument_id'),
        nullable= False
    )

    close_price = Column(Numeric(24, 10), nullable= False)
    price_date = Column(Date, nullable= False)
    created_at = Column(DateTime(timezone= True), server_default= func.now())

    instrument = relationship('Instrument')

    __table_args__ = (
        UniqueConstraint('instrument_id', 'price_date', name='uq_daily_price_instrument_date'),
        CheckConstraint('close_price >= 0', name='chk_daily_price_non_negative'),
    )