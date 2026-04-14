from fastapi import APIRouter, Depends, HTTPException, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import Optional
import json

from app.db.database import get_db
from app.models.template import Template
from app.models.workspace import Workspace
from app.models.user import User
from app.api.v1.auth import get_current_user
from app.api.v1.workspaces import get_workspace_and_check_access
from app.core.exceptions import NotFoundException, BadRequestException

router = APIRouter()


class TemplateCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None
    content: dict  # draft_content.json


class TemplateResponse(BaseModel):
    id: str
    name: str
    description: Optional[str]
    category: Optional[str]
    tags: Optional[list[str]]
    metadata: dict
    thumbnail_url: Optional[str]
    is_public: bool
    usage_count: int

    class Config:
        from_attributes = True


class TemplateDetailResponse(TemplateResponse):
    content: dict


@router.get("", response_model=list[TemplateResponse])
async def list_templates(
    workspace_id: UUID,
    category: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    query = select(Template).where(Template.workspace_id == workspace_id)
    if category:
        query = query.where(Template.category == category)

    result = await db.execute(query.order_by(Template.created_at.desc()))
    templates = result.scalars().all()

    return [
        TemplateResponse(
            id=str(t.id),
            name=t.name,
            description=t.description,
            category=t.category,
            tags=t.tags,
            metadata=t.metadata or {},
            thumbnail_url=t.thumbnail_url,
            is_public=t.is_public,
            usage_count=t.usage_count,
        )
        for t in templates
    ]


@router.post("", response_model=TemplateResponse)
async def create_template(
    workspace_id: UUID,
    data: TemplateCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    # Extract metadata from content
    metadata = _extract_metadata(data.content)

    template = Template(
        workspace_id=workspace_id,
        name=data.name,
        description=data.description,
        category=data.category,
        tags=data.tags,
        content=data.content,
        metadata=metadata,
        created_by=current_user.id,
    )
    db.add(template)
    await db.commit()
    await db.refresh(template)

    return TemplateResponse(
        id=str(template.id),
        name=template.name,
        description=template.description,
        category=template.category,
        tags=template.tags,
        metadata=template.metadata or {},
        thumbnail_url=template.thumbnail_url,
        is_public=template.is_public,
        usage_count=template.usage_count,
    )


@router.get("/{template_id}", response_model=TemplateDetailResponse)
async def get_template(
    workspace_id: UUID,
    template_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(
        select(Template)
        .where(Template.id == template_id)
        .where(Template.workspace_id == workspace_id)
    )
    template = result.scalar_one_or_none()

    if not template:
        raise NotFoundException("Template not found")

    return TemplateDetailResponse(
        id=str(template.id),
        name=template.name,
        description=template.description,
        category=template.category,
        tags=template.tags,
        metadata=template.metadata or {},
        thumbnail_url=template.thumbnail_url,
        is_public=template.is_public,
        usage_count=template.usage_count,
        content=template.content,
    )


@router.delete("/{template_id}")
async def delete_template(
    workspace_id: UUID,
    template_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(
        select(Template)
        .where(Template.id == template_id)
        .where(Template.workspace_id == workspace_id)
    )
    template = result.scalar_one_or_none()

    if not template:
        raise NotFoundException("Template not found")

    await db.delete(template)
    await db.commit()

    return {"message": "Template deleted"}


def _extract_metadata(content: dict) -> dict:
    """Extract metadata from draft_content.json"""
    try:
        tracks = content.get("tracks", [])
        track_count = len(tracks)
        segment_count = sum(len(t.get("segments", [])) for t in tracks)
        return {
            "track_count": track_count,
            "segment_count": segment_count,
        }
    except Exception:
        return {}
