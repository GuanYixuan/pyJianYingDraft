import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID, JSON, ARRAY
from sqlalchemy.orm import relationship
from app.db.database import Base


class Template(Base):
    __tablename__ = "templates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id", ondelete="CASCADE"))
    name = Column(String(255), nullable=False)
    description = Column(Text)
    category = Column(String(100))  # marketing/social/education
    tags = Column(ARRAY(String))

    # Template content stored as JSON (parsed draft_content.json structure)
    content = Column(JSON, nullable=False)

    # Extracted metadata for quick listing
    metadata = Column(JSON, default={})  # {duration, track_count, material_count}

    thumbnail_url = Column(String(500))
    is_public = Column(Boolean, default=False)  # Marketplace templates
    usage_count = Column(Integer, default=0)

    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    workspace = relationship("Workspace", back_populates="templates")
    drafts = relationship("Draft", back_populates="source_template")
