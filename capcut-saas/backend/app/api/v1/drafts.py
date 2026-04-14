from fastapi import APIRouter, Depends, HTTPException, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import Optional

from app.db.database import get_db
from app.models.draft import Draft
from app.models.template import Template
from app.models.workspace import Workspace
from app.models.user import User
from app.api.v1.auth import get_current_user
from app.api.v1.workspaces import get_workspace_and_check_access
from app.core.exceptions import NotFoundException, BadRequestException
from app.services.draft_service import DraftService

router = APIRouter()


class DraftGenerateRequest(BaseModel):
    template_id: UUID
    materials_mapping: dict  # {template_material_name: material_uuid}
    text_replacements: Optional[dict] = None  # {segment_id: new_text}
    options: Optional[dict] = None  # {width, height, fps}


class DraftResponse(BaseModel):
    id: str
    name: str
    metadata: dict
    status: str
    source_template_id: Optional[str]

    class Config:
        from_attributes = True


class DraftDetailResponse(DraftResponse):
    content: dict


@router.get("", response_model=list[DraftResponse])
async def list_drafts(
    workspace_id: UUID,
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(
        select(Draft)
        .where(Draft.workspace_id == workspace_id)
        .where(Draft.project_id == project_id)
        .order_by(Draft.created_at.desc())
    )
    drafts = result.scalars().all()

    return [
        DraftResponse(
            id=str(d.id),
            name=d.name,
            metadata=d.metadata or {},
            status=d.status,
            source_template_id=str(d.source_template_id) if d.source_template_id else None,
        )
        for d in drafts
    ]


@router.post("/generate", response_model=DraftResponse)
async def generate_draft(
    workspace_id: UUID,
    project_id: UUID,
    request: DraftGenerateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    # Get template
    result = await db.execute(
        select(Template)
        .where(Template.id == request.template_id)
        .where(Template.workspace_id == workspace_id)
    )
    template = result.scalar_one_or_none()
    if not template:
        raise NotFoundException("Template not found")

    # Generate draft using DraftService
    draft_service = DraftService(db)
    generated = await draft_service.generate_from_template(
        template=template,
        project_id=project_id,
        materials_mapping=request.materials_mapping,
        text_replacements=request.text_replacements or {},
        options=request.options or {},
        user_id=current_user.id,
    )

    return DraftResponse(
        id=str(generated.id),
        name=generated.name,
        metadata=generated.metadata or {},
        status=generated.status,
        source_template_id=str(generated.source_template_id) if generated.source_template_id else None,
    )


@router.get("/{draft_id}", response_model=DraftDetailResponse)
async def get_draft(
    workspace_id: UUID,
    project_id: UUID,
    draft_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(
        select(Draft)
        .where(Draft.id == draft_id)
        .where(Draft.workspace_id == workspace_id)
        .where(Draft.project_id == project_id)
    )
    draft = result.scalar_one_or_none()

    if not draft:
        raise NotFoundException("Draft not found")

    return DraftDetailResponse(
        id=str(draft.id),
        name=draft.name,
        metadata=draft.metadata or {},
        status=draft.status,
        source_template_id=str(draft.source_template_id) if draft.source_template_id else None,
        content=draft.content,
    )


@router.get("/{draft_id}/export")
async def export_draft(
    workspace_id: UUID,
    project_id: UUID,
    draft_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Export draft as JSON for download"""
    await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(
        select(Draft)
        .where(Draft.id == draft_id)
        .where(Draft.workspace_id == workspace_id)
        .where(Draft.project_id == project_id)
    )
    draft = result.scalar_one_or_none()

    if not draft:
        raise NotFoundException("Draft not found")

    return {
        "draft_content.json": draft.content,
        "draft_meta_info.json": {
            "name": draft.name,
            "description": "",
            "create_time": str(draft.created_at),
            "modify_time": str(draft.updated_at),
            "version": "3.0",
            "draft_id": str(draft.id),
        },
    }


@router.delete("/{draft_id}")
async def delete_draft(
    workspace_id: UUID,
    project_id: UUID,
    draft_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(
        select(Draft)
        .where(Draft.id == draft_id)
        .where(Draft.workspace_id == workspace_id)
        .where(Draft.project_id == project_id)
    )
    draft = result.scalar_one_or_none()

    if not draft:
        raise NotFoundException("Draft not found")

    await db.delete(draft)
    await db.commit()

    return {"message": "Draft deleted"}
