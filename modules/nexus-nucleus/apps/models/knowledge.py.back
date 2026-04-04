class KnowledgeBase(NucleusBase, table=True):
    """Project-Bound Context: The Shared Reality (Form 6)"""
    __table_args__ = {"schema": "nucleus"}
    name: str
    target_project_id: uuid.UUID = Field(foreign_key="nucleus.project.id")
    embedding_model_id: uuid.UUID = Field(foreign_key="nucleus.model.id")
    sync_frequency: str = Field(default="Manual") # Manual, Hourly, Daily
    access_level: str = Field(default="Shared") # Private, Shared
    
    files: List["File"] = Relationship(back_populates="kb")

class File(NucleusBase, table=True):
    """The raw source documents (PDF, MD, Code)"""
    __table_args__ = {"schema": "nucleus"}
    kb_id: uuid.UUID = Field(foreign_key="nucleus.knowledgebase.id")
    uploader_id: uuid.UUID = Field(foreign_key="nucleus.user.id")
    file_name: str
    file_path: str # Path on the local server volume
    alias: Optional[str] = None # Custom name for AI referencing
    
    kb: KnowledgeBase = Relationship(back_populates="files")