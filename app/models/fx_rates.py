import uuid6
from sqlalchemy import Column, String, Date, Numeric, DateTime, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base

class FxRate(Base):
    __tablename__ = 'fx_rates'

    fx_rate_id = Column(
        UUID(as_uuid= True),
        primary_key= True,
        index= True,
        default= uuid6.uuid7
    )

    base_currency = Column(String(3), ForeignKey('currencies.currency_code'), nullable= False)
    quote_currency = Column(String(3), ForeignKey('currencies.currency_code'), nullable= False)
    rate_date = Column(Date, nullable= False)

    rate = Column(Numeric(24, 10), nullable=False)
    source = Column(String, nullable=False, default='MANUAL')
    fetched_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint('base_currency', 'quote_currency', 'rate_date', 'source', name= 'unique_fx_rate_daily'),
        CheckConstraint('rate > 0', name= 'check_fx_rate_positive'),
        CheckConstraint('base_currency != quote_currency', name= 'check_fx_different_currencies')
    )
