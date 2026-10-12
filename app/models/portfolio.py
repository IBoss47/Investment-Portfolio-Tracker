import uuid6
from sqlalchemy import Column, String, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func
from sqlalchemy.orm import relationship

from app.database import Base

class Portfolio(Base):
    __tablename__ = 'portfolios'

    portfolio_id = Column(
        UUID(as_uuid= True),
        primary_key= True,
        index= True,
        default= uuid6.uuid7
    )
    user_id = Column(
        UUID(as_uuid= True),
        ForeignKey('users.user_id'),
        nullable= False
    )
    base_currency = Column(
        String(3),
        ForeignKey('currencies.currency_code'),
        nullable=False
    )

    name = Column(String, nullable= False)
    inception_date = Column(Date, nullable= False)
    created_at = Column(DateTime(timezone= True), server_default= func.now())

    user = relationship('User')
    currency = relationship('Currency')