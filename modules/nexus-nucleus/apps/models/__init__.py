# modules/nexus-nucleus/apps/models/__init__.py
# from .base import NucleusBase
# from .governance import User, Human, Group, Permission, PermissionMapping, GroupUserMapping
# from .intelligence import Model, Agent, Persona, MCPServer, AgentMCPMapping, KnowledgeBase, File
# from .workspace import Project, ProjectMember, Channel, ChatTopic, ChatLine, ReadMarker

# # This is the object Alembic needs
# from sqlmodel import SQLModel
# target_metadata = SQLModel.metadata


# from apps.db.base import Base
# from apps.modules.governance.models import (
#     User, Human, Group, 
#     # Permission, PermissionMapping, GroupUserMapping
# )
# # Import other module models here as you convert them

# # This is what env.py will import

# apps/models/__init__.py

# from apps.modules.governance.models import (
#     User,
#     Human,
#     UserType,
#     # Group,         <-- Comment these out
#     # Permission,    <-- Comment these out
# )
# target_metadata = Base.metadata

# apps/models/__init__.py

# 1. First, import the Base (This defines the metadata object)
from apps.db.base import Base 

# 2. Then, import your models (This registers them to the Base)
from apps.modules.governance.models import User, Human, UserType
# from apps.history.models import Conversation, Message # If you are ready for these

# 3. Finally, define the target_metadata for Alembic
target_metadata = Base.metadata