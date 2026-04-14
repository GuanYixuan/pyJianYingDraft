import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, BigInteger, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base


class FinalVideo(Base):
    __tablename__ = "final_videos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    workspace_id = Column(UUID(as_uuid=True), ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False)

    # Video info
    filename = Column(String(255), nullable=False)
    storage_path = Column(String(500), nullable=False)  # MinIO path
    duration_ms = Column(BigInteger)  # 时长(毫秒)
    thumbnail_url = Column(String(500))  # 缩略图
    file_size_bytes = Column(BigInteger)

    # Source draft
    source_draft_id = Column(UUID(as_uuid=True), ForeignKey("drafts.id"))

    # Publish status
    # {douyin: {published: false, video_id: null, url: null}, wechat_channels: {published: false}}
    publish_status = Column(JSON, default=lambda: {"douyin": {"published": False}, "wechat_channels": {"published": False}})

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    order = relationship("Order", back_populates="final_videos")
    user = relationship("User")
    workspace = relationship("Workspace")
    source_draft = relationship("Draft")
    publish_records = relationship("PublishRecord", back_populates="final_video")
