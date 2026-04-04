import uuid
from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum
from typing import Optional
import uuid
from sqlmodel import Field, Relationship
from .base import NucleusBase

class UserType(str, Enum):
    HUMAN = "human"
    PERSONA = "persona"

class User(NucleusBase, table=True):
    """The Global Identity (Passport). No Credentials here."""
    __table_args__ = {"schema": "nucleus"}

    username: str = Field(unique=True, index=True) # @faisal or @nexus-bot
    full_name: str # "Faisal" or "Nexus Architect"
    user_type: UserType = Field(index=True) # human | persona
    
    role: str = Field(default="member")
    is_active: bool = Field(default=True)

    # Relationships to the "Secret" profiles
    human_profile: Optional["Human"] = Relationship(
        back_populates="user", 
        sa_relationship_kwargs={"uselist": False}
    )
    persona_profile: Optional["Persona"] = Relationship(
        back_populates="user", 
        sa_relationship_kwargs={"uselist": False}
    )
    


class Human(NucleusBase, table=True):
    """The 'Private' side of a Human User."""
    __table_args__ = {"schema": "nucleus"}
    
    user_id: uuid.UUID = Field(foreign_key="nucleus.user.id", unique=True)
    
    # Credentials stay HERE only
    email: str = Field(unique=True, index=True)
    hashed_password: str 
    
    user: "User" = Relationship(back_populates="human_profile")

class Group(NucleusBase, table=True):
    name: str # e.g., "Dev Team"
    description: Optional[str] = None

class Permission(NucleusBase, table=True):
    code: str = Field(unique=True) # e.g., "can_manage_kb"
    description: str

class PermissionMapping(SQLModel, table=True):
    """RBAC Logic: Links Groups to their specific Rights."""
    __table_args__ = {"schema": "nucleus"}
    group_id: uuid.UUID = Field(foreign_key="nucleus.group.id", primary_key=True)
    permission_id: uuid.UUID = Field(foreign_key="nucleus.permission.id", primary_key=True)

class GroupUserMapping(SQLModel, table=True):
    """Links Users to Groups."""
    __table_args__ = {"schema": "nucleus"}
    group_id: uuid.UUID = Field(foreign_key="nucleus.group.id", primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="nucleus.user.id", primary_key=True)