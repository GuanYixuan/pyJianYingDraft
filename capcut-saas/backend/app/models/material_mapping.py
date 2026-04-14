import uuid
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base


class MaterialMapping(Base):
    """Maps template materials to actual materials in drafts"""
    __tablename__ = "material_mappings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    draft_id = Column(UUID(as_uuid=True), ForeignKey("drafts.id", ondelete="CASCADE"))
    material_id = Column(UUID(as_uuid=True), ForeignKey("materials.id", ondelete="SET NULL"))

    # The material_id as it appears in the draft JSON
    draft_material_id = Column(String(100), nullable=False)

    # For template mode - maps template material name to actual material UUID
    template_material_name = Column(String(255))

    __table_args__ = (
        UniqueConstraint('draft_id', 'draft_material_id', name='uq_draft_material'),
    )
