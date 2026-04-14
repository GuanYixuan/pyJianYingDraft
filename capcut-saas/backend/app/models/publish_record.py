import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base


class PublishRecord(Base):
    __tablename__ = "publish_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    final_video_id = Column(UUID(as_uuid=True), ForeignKey("final_videos.id", ondelete="CASCADE"), nullable=False)

    # Platform: douyin/wechat_channels
    platform = Column(String(50), nullable=False)

    # Platform response
    external_video_id = Column(String(255))  # 平台返回ID
    external_url = Column(String(500))  # 平台返回链接

    # Status: pending/success/failed
    status = Column(String(20), default="pending")

    # Error message if failed
    error_message = Column(String(1000))

    # Timestamps
    published_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    final_video = relationship("FinalVideo", back_populates="publish_records")
