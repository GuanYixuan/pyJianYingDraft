import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text, ARRAY, BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False)

    # Requirements
    requirements = Column(Text)  # 需求描述
    industry = Column(String(100))  # 行业
    product = Column(String(255))  # 产品名称
    region = Column(String(100))  # 地区

    # Materials
    material_ids = Column(ARRAY(UUID(as_uuid=True)), default=[])  # 关联素材

    # Assignment
    assigned_operator_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    # Status: pending/assigned/processing/completed/failed
    status = Column(String(20), default="pending")

    # Priority: low/normal/high/urgent
    priority = Column(String(20), default="normal")

    # AI generated script
    ai_script = Column(Text)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", foreign_keys=[user_id])
    operator = relationship("User", foreign_keys=[assigned_operator_id])
    workspace = relationship("Workspace")
    final_videos = relationship("FinalVideo", back_populates="order")
