import uuid
from datetime import datetime
from sqlalchemy import Column, String, BigInteger, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base


class Material(Base):
    __tablename__ = "materials"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id", ondelete="CASCADE"))
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    type = Column(String(20), nullable=False)  # video/audio/image
    filename = Column(String(255), nullable=False)
    original_filename = Column(String(255))
    file_size_bytes = Column(BigInteger, nullable=False)
    mime_type = Column(String(100))

    # Storage info
    storage_path = Column(String(500), nullable=False)  # MinIO path
    cdn_url = Column(String(500))

    # Media metadata
    duration_ms = Column(BigInteger)  # for video/audio
    width = Column(Integer)  # for video/image
    height = Column(Integer)  # for video/image

    # pyJianYingDraft material mapping
    material_id = Column(String(100))  # The material_id used in draft JSON

    status = Column(String(20), default="pending")  # pending/processing/ready/failed

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    workspace = relationship("Workspace", back_populates="materials")
