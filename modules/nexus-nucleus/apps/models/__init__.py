# modules/nexus-nucleus/apps/models/__init__.py
# from .base import NucleusBase
# from .governance import User, Human, Group, Permission, PermissionMapping, GroupUserMapping
# from .intelligence import Model, Agent, Persona, MCPServer, AgentMCPMapping, KnowledgeBase, File
# from .workspace import Project, ProjectMember, Channel, ChatTopic, ChatLine, ReadMarker

# # This is the object Alembic needs
# from sqlmodel import SQLModel
# target_metadata = SQLModel.metadata


from .base import NucleusBase
from .governance import User, Human, Group, Permission, PermissionMapping, GroupUserMapping

# Temporarily disabled to isolate the base setup
# from .intelligence import ...
# from .workspace import ...

from sqlmodel import SQLModel
target_metadata = SQLModel.metadata