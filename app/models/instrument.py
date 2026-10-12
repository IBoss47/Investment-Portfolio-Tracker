import uuid6
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database import Base

class Instrument(Base):
    __tablename__ = 'instruments'

    instrument_id = Column(
        UUID(as_uuid= True),
        primary_key= True,
        index= True,
        default= uuid6.uuid7
    )
    currency = Column(
        String(3),
        ForeignKey('currencies.currency_code'),
        nullable= False
    )

    symbol = Column(String, nullable= False)
    exchange_market = Column(String, nullable= False)
    asset_type = Column(String, nullable= False)

    __table_args__ = (
        UniqueConstraint(
            'symbol', 'exchange_market', name= 'unique_instrument_symbol_exchange'
        ),
        CheckConstraint(
            "asset_type IN ('STOCK', 'ETF')", name= 'check_instrument_asset_type'
        )
    )
