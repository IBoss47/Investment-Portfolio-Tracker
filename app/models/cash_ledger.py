import uuid6
from sqlalchemy import Column, String, Numeric, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class CashLedgerEntry(Base):
    __tablename__ = 'cash_ledger_entries'

    cash_entry_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid6.uuid7
    )
    transaction_id = Column(
        UUID(as_uuid=True),
        ForeignKey('transactions.transaction_id'),
        nullable=False
    )
    portfolio_id = Column(
        UUID(as_uuid=True),
        ForeignKey('portfolios.portfolio_id'),
        nullable=False
    )
    currency_code = Column(
        String(3),
        ForeignKey('currencies.currency_code'),
        nullable=False
    )

    amount_signed = Column(Numeric(24, 8), nullable=False)
    entry_role = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        CheckConstraint(
            "entry_role IN ('TRADE', 'DIVIDEND', 'DEPOSIT', 'WITHDRAWAL', 'FEE_TAX', 'FX_OUT', 'FX_IN', 'ADJUSTMENT')",
            name='chk_cash_entry_role'
        ),
    )

    transaction = relationship('Transaction')
    portfolio = relationship('Portfolio')