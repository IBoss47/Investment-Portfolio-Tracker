import uuid6
from sqlalchemy import Column, String
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

    symbol = Column(String, nullable= False)
    exchange_market = Column(String, nullable= False)
    asset_type = Column(String, nullable= False)
