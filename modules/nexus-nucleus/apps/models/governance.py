import uuid
from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class NucleusBase(SQLModel):
    """The Root Lock for all Nucleus entities."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    company_id: uuid.UUID = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    __table_args__ = {"schema": "nucleus"}

class User(NucleusBase, table=True):
    email: str = Field(unique=True, index=True)
    full_name: str
    hashed_password: str
    role: str = Field(default="member") # Admin, Member, Guest
    is_active: bool = Field(default=True)

class Group(NucleusBase, table=True):
    name: str # e.g., "Dev Team"
    description: Optional[str] = None

class Permission(NucleusBase, table=True):
    code: str = Field(unique=True) # e.g., "can_manage_kb"
    description: str