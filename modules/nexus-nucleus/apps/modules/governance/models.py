import uuid
from enum import Enum
from typing import Optional, List
from sqlalchemy import String, ForeignKey, UniqueConstraint, \
    Boolean, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from apps.db.base import BaseModel

class UserType(str, Enum):
    HUMAN = "human"
    PERSONA = "persona"

class User(BaseModel):
    """
    The Global Identity (Passport). 
    Contains public profile data but no credentials.
    """
    __tablename__ = "user"
    __table_args__ = (
        UniqueConstraint("username", "company_id", name="uq_user_username_tenant"),
        {"schema": "nucleus"}
    )

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String(50), index=True) # @faisal or @nexus-bot
    full_name: Mapped[str] = mapped_column(String(100))
    user_type: Mapped[UserType] = mapped_column(SAEnum(UserType), index=True)
    
    role: Mapped[str] = mapped_column(String(30), default="member")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relationships
    # uselist=False ensures 1-to-1 mapping
    human_profile: Mapped[Optional["Human"]] = relationship(
        back_populates="user", 
        uselist=False,
        cascade="all, delete-orphan"
    )
    # Persona will be defined in the intelligence module
    persona_profile: Mapped[Optional["Persona"]] = relationship(
        "Persona",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    # M2M Relationships
    # groups: Mapped[List["Group"]] = relationship(
    #     secondary="nucleus.group_user_mapping", 
    #     back_populates="users"
    # )


class Human(BaseModel):
    """
    The 'Private' side of a Human User. 
    Credentials live here.
    """
    __tablename__ = "human"
    __table_args__ = {"schema": "nucleus"}
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("nucleus.user.id", ondelete="CASCADE"), 
        unique=True
    )
    
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    
    user: Mapped["User"] = relationship(back_populates="human_profile")


# class Group(BaseModel):
#     __tablename__ = "group"
#     __table_args__ = {"schema": "nucleus"}

#     id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
#     name: Mapped[str] = mapped_column(String(100))
#     description: Mapped[Optional[str]] = mapped_column(String(255))

#     users: Mapped[List["User"]] = relationship(
#         secondary="nucleus.group_user_mapping", 
#         back_populates="groups"
#     )
#     permissions: Mapped[List["Permission"]] = relationship(
#         secondary="nucleus.permission_mapping", 
#         back_populates="groups"
#     )


# class Permission(Base, TimestampMixin):
#     __tablename__ = "permission"
#     __table_args__ = {"schema": "nucleus"}

#     id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
#     code: Mapped[str] = mapped_column(String(50), unique=True) # e.g., "can_manage_kb"
#     description: Mapped[str] = mapped_column(String(255))

#     groups: Mapped[List["Group"]] = relationship(
#         secondary="nucleus.permission_mapping", 
#         back_populates="permissions"
#     )


# # --- MANY-TO-MANY MAPPING TABLES ---

# class PermissionMapping(Base):
#     """RBAC Logic: Links Groups to their specific Rights."""
#     __tablename__ = "permission_mapping"
#     __table_args__ = {"schema": "nucleus"}

#     group_id: Mapped[uuid.UUID] = mapped_column(
#         ForeignKey("nucleus.group.id", ondelete="CASCADE"), 
#         primary_key=True
#     )
#     permission_id: Mapped[uuid.UUID] = mapped_column(
#         ForeignKey("nucleus.permission.id", ondelete="CASCADE"), 
#         primary_key=True
#     )


# class GroupUserMapping(Base):
#     """Links Users to Groups."""
#     __tablename__ = "group_user_mapping"
#     __table_args__ = {"schema": "nucleus"}

#     group_id: Mapped[uuid.UUID] = mapped_column(
#         ForeignKey("nucleus.group.id", ondelete="CASCADE"), 
#         primary_key=True
#     )
#     user_id: Mapped[uuid.UUID] = mapped_column(
#         ForeignKey("nucleus.user.id", ondelete="CASCADE"), 
#         primary_key=True
#     )