import uuid
from typing import Optional, List, Dict, Any
from sqlmodel import SQLModel, Field, Relationship, Column, JSON, Text
from .base import NucleusBase
from sqlalchemy import CheckConstraint, UniqueConstraint
from typing import Optional
import uuid
from sqlmodel import Field, Column, Text
from .base import NucleusBase


# --- Mapping Tables (Many-to-Many) ---

class AgentMCPMapping(SQLModel, table=True):
    """Links Agents to their allowed MCP Tools."""
    __table_args__ = {"schema": "nucleus"}
    agent_id: uuid.UUID = Field(foreign_key="nucleus.agent.id", primary_key=True)
    mcp_server_id: uuid.UUID = Field(foreign_key="nucleus.mcpserver.id", primary_key=True)

# --- Core Intelligence Entities ---

class Model(NucleusBase, table=True):
    """The Raw Engine (Technical Config)."""
    __table_args__ = {"schema": "nucleus"}
    
    provider: str # Ollama, OpenAI, etc.
    endpoint_url: str
    api_key_masked: str
    model_id_name: str # e.g., llama3:70b
    temperature: float = Field(default=0.7)
    
    owner_id: uuid.UUID = Field(foreign_key="nucleus.user.id")
    # Link back to personas using this model
    personas: List["Persona"] = Relationship(back_populates="provider_model")

class Agent(NucleusBase, table=True):
    """The Specialized Worker (Instructions + Tools)."""
    __table_args__ = {"schema": "nucleus"}
    
    system_instructions: str = Field(sa_column=Column(Text))
    safety_mode: bool = Field(default=True)
    
    # The 'Brain' this agent uses
    base_model_id: uuid.UUID = Field(foreign_key="nucleus.model.id")
    
    owner_id: uuid.UUID = Field(foreign_key="nucleus.user.id")
    
    # Links
    mcp_servers: List["MCPServer"] = Relationship(
        back_populates="agents", link_model=AgentMCPMapping
    )
    personas: List["Persona"] = Relationship(back_populates="provider_agent")


class Persona(NucleusBase, table=True):
    """
    The Identity Proxy. 
    Unique per Prompt + (Model OR Agent) + Project + Company.
    """
    __table_args__ = (
        # 1. THE XOR CONSTRAINT: Ensures either model or agent is set, not both/neither.
        CheckConstraint(
            "(provider_model_id IS NOT NULL AND provider_agent_id IS NULL) OR "
            "(provider_model_id IS NULL AND provider_agent_id IS NOT NULL)",
            name="check_persona_source_xor"
        ),
        # 2. THE IDENTITY CONSTRAINT: Prevents duplicate personalities in the same workspace.
        UniqueConstraint(
            "persona_prompt", 
            "provider_model_id", 
            "provider_agent_id", 
            "project_id", 
            "company_id", 
            name="uq_persona_identity"
        ),
        {"schema": "nucleus"},
    )

    user_id: uuid.UUID = Field(foreign_key="nucleus.user.id", unique=True)
    project_id: uuid.UUID = Field(foreign_key="nucleus.project.id", index=True)

    provider_model_id: Optional[uuid.UUID] = Field(default=None, foreign_key="nucleus.model.id")
    provider_agent_id: Optional[uuid.UUID] = Field(default=None, foreign_key="nucleus.agent.id")

    # ORM Relationships for easy access
    provider_model: Optional[Model] = Relationship(back_populates="personas")
    provider_agent: Optional[Agent] = Relationship(back_populates="personas")
    
    persona_prompt: Optional[str] = Field(default=None, sa_column=Column(Text))
    tone_style: str = Field(default="Balanced")    

class MCPServer(NucleusBase, table=True):
    """The Capability Layer (Form 5) - SSH, SQL, GitHub Bridge."""
    __table_args__ = {"schema": "nucleus"}
    
    name: str = Field(unique=True) # e.g., "SSH-Bridge"
    transport: str # "stdio" | "sse"
    command_url: str # Local path or URL
    env_vars: Optional[Dict[str, str]] = Field(default_factory=dict, sa_column=Column(JSON))
    
    agents: List[Agent] = Relationship(
        back_populates="mcp_servers", link_model=AgentMCPMapping
    )
