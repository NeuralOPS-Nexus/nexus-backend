import uuid
from datetime import datetime, timezone
from sqlalchemy import DateTime, func, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

class Base(DeclarativeBase):
    """The SQLAlchemy 2.0 Master Base."""
    pass

class BaseModel(Base):
    __abstract__ = True

    company_id: Mapped[uuid.UUID] = mapped_column(index=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )