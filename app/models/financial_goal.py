import uuid6
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class FinancialGoal(Base):
    __tablename__ = 'financial_goals'

    goal_id = Column(
        UUID(as_uuid= True),
        primary_key= True,
        index= True,
        default= uuid6.uuid7
    )
    portfolio_id = Column(
        UUID(as_uuid= True),
        ForeignKey('portfolios.portfolio_id'),
        nullable= False
    )
    goal_type = Column(String, nullable= False)
    target_wealth_amount = Column(Numeric(24, 10), nullable= True)
    target_monthly_income = Column(Numeric(24, 10), nullable=True)
    expected_interest_rate = Column(Numeric(5, 2), nullable= False)
    target_date = Column(Date, nullable= False)

    portfolio = relationship("Portfolio")

