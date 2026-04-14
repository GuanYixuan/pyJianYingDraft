import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255))
    avatar_url = Column(String(500))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # SaaS extension fields
    industry = Column(String(100))  # 行业: "美妆", "餐饮", "电商"
    product = Column(String(255))    # 产品名称
    region = Column(String(100))    # 地区: "华东", "华北"
    role = Column(String(20), default="user")  # user/operator/admin

    # Relationships
    workspace_memberships = relationship("WorkspaceMember", back_populates="user")
