# modules/nexus-nucleus/apps/models/__init__.py
# from .base import NucleusBase
# from .governance import User, Human, Group, Permission, PermissionMapping, GroupUserMapping
# from .intelligence import Model, Agent, Persona, MCPServer, AgentMCPMapping, KnowledgeBase, File
# from .workspace import Project, ProjectMember, Channel, ChatTopic, ChatLine, ReadMarker

# # This is the object Alembic needs
# from sqlmodel import SQLModel
# target_metadata = SQLModel.metadata


from apps.db.base import Base
from apps.modules.governance.models import (
    User, Human, Group, Permission, PermissionMapping, GroupUserMapping
)
# Import other module models here as you convert them

# This is what env.py will import
target_metadata = Base.metadata