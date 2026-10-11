import uuid6
from sqlalchemy import Column, String, Date, DateTime, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func
from sqlalchemy.orm import relationship

from app.database import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(
        UUID(as_uuid= True),
        primary_key= True,
        index= True,
        default= uuid6.uuid7
    )
    instrument_id = Column(
        UUID(as_uuid= True),
        ForeignKey('instruments.instrument_id'),
        nullable= True
    )
    portfolio_id = Column(
        UUID(as_uuid= True),
        ForeignKey('portfolio.portfolio_id')
    )

    transaction_type = Column(String, nullable= False)
    executed_price = Column(Numeric(24, 10), nullable= True)
    unit_delta = Column(Numeric(24, 10), nullable= True)
    fee_amount = Column(Numeric(24, 10), nullable=True)

    transaction_at = Column(Date, nullable= False)
    create_at = Column(DateTime(timezone= True), server_default= func.now())

    portfolio = relationship('Portfolio')
    instrument = relationship('Instrument')
