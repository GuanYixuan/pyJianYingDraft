import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base


class Draft(Base):
    __tablename__ = "drafts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"))
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id", ondelete="CASCADE"))

    name = Column(String(255), nullable=False)

    # Draft content as JSON (full draft_content.json structure)
    content = Column(JSON, nullable=False)

    # Reference to source template (if created from template)
    source_template_id = Column(UUID(as_uuid=True), ForeignKey("templates.id"))

    # Draft metadata
    metadata = Column(JSON, default={})  # {duration, track_count, segment_count}

    # Status
    # Draft status: draft/published/archived
    # For SaaS: draft/published/archived/processing/completed/failed
    status = Column(String(20), default="draft")
    processing_status = Column(String(20), default=None)  # pending/processing/completed/failed (for SaaS orders)

    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    project = relationship("Project", back_populates="drafts")
    source_template = relationship("Template", back_populates="drafts")
