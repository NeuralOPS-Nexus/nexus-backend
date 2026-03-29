import uuid
from datetime import datetime, timezone
from typing import Any, Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime, text
from sqlalchemy.orm import declared_attr

class NucleusBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    company_id: uuid.UUID = Field(index=True, nullable=False)

    # We add the type hint '-> Any' to stop Pydantic from complaining.
    # SQLAlchemy will still execute the function to get the Column object.
    @declared_attr
    def created_at(cls) -> Any:
        return Column(
            DateTime(timezone=True), 
            nullable=False, 
            server_default=text("now()")
        )

    @declared_attr
    def updated_at(cls) -> Any:
        return Column(
            DateTime(timezone=True), 
            nullable=False, 
            server_default=text("now()"),
            onupdate=lambda: datetime.now(timezone.utc)
        )