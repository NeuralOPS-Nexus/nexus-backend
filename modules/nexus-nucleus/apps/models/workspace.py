class Project(NucleusBase, table=True):
    name: str
    description: Optional[str] = None
    # MagicDNS URL for Tailscale access
    instance_url: Optional[str] = None 

class ProjectMember(SQLModel, table=True):
    """Many-to-Many mapping for Humans in Projects."""
    __table_args__ = {"schema": "nucleus"}
    project_id: uuid.UUID = Field(foreign_key="nucleus.project.id", primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="nucleus.user.id", primary_key=True)

class Channel(NucleusBase, table=True):
    name: str # e.g., #sre-chat
    project_id: uuid.UUID = Field(foreign_key="nucleus.project.id")

class ChatTopic(NucleusBase, table=True):
    """Threading logic to prevent scroll fatigue."""
    name: str 
    channel_id: uuid.UUID = Field(foreign_key="nucleus.channel.id")

class ChatLine(NucleusBase, table=True):
    """Message history with Snippet support."""
    topic_id: uuid.UUID = Field(foreign_key="nucleus.chattopic.id")
    sender_id: uuid.UUID = Field(index=True)
    sender_type: str # human | agent | persona | model
    content: str
    
    # Snippet support for interactive UI
    snippet_type: Optional[str] = None # terminal, graph, code, form
    snippet_data: Optional[str] = None # JSON string of structured data