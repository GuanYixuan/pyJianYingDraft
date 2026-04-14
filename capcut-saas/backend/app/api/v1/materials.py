import os
import uuid
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import Optional
import aiofiles

from app.db.database import get_db
from app.models.material import Material
from app.models.workspace import Workspace
from app.models.user import User
from app.api.v1.auth import get_current_user
from app.api.v1.workspaces import get_workspace_and_check_access
from app.core.exceptions import NotFoundException, BadRequestException
from app.config import settings
from app.services.storage_service import StorageService

router = APIRouter()
storage_service = StorageService()


class MaterialResponse(BaseModel):
    id: str
    type: str
    filename: str
    file_size_bytes: int
    mime_type: Optional[str]
    storage_path: str
    cdn_url: Optional[str]
    duration_ms: Optional[int]
    width: Optional[int]
    height: Optional[int]
    status: str

    class Config:
        from_attributes = True


@router.get("", response_model=list[MaterialResponse])
async def list_materials(
    workspace_id: UUID,
    project_id: Optional[UUID] = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    query = select(Material).where(Material.workspace_id == workspace_id)
    if project_id:
        query = query.where(Material.project_id == project_id)

    result = await db.execute(query.order_by(Material.created_at.desc()))
    materials = result.scalars().all()

    return [
        MaterialResponse(
            id=str(m.id),
            type=m.type,
            filename=m.filename,
            file_size_bytes=m.file_size_bytes,
            mime_type=m.mime_type,
            storage_path=m.storage_path,
            cdn_url=m.cdn_url,
            duration_ms=m.duration_ms,
            width=m.width,
            height=m.height,
            status=m.status,
        )
        for m in materials
    ]


@router.post("/upload", response_model=MaterialResponse)
async def upload_material(
    workspace_id: UUID,
    file: UploadFile = File(...),
    project_id: Optional[UUID] = Form(None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    # Determine material type
    content_type = file.content_type or "application/octet-stream"
    if content_type.startswith("video/"):
        material_type = "video"
    elif content_type.startswith("audio/"):
        material_type = "audio"
    elif content_type.startswith("image/"):
        material_type = "image"
    else:
        raise BadRequestException(f"Unsupported file type: {content_type}")

    # Generate unique filename
    ext = os.path.splitext(file.filename)[1] if file.filename else ""
    unique_filename = f"{uuid.uuid4()}{ext}"
    storage_path = f"workspaces/{workspace_id}/materials/{unique_filename}"

    # Save file to MinIO
    file_content = await file.read()
    await storage_service.upload_file(storage_path, file_content, content_type)

    # Create material record
    material = Material(
        workspace_id=workspace_id,
        project_id=project_id,
        user_id=current_user.id,
        type=material_type,
        filename=unique_filename,
        original_filename=file.filename,
        file_size_bytes=len(file_content),
        mime_type=content_type,
        storage_path=storage_path,
        status="processing",  # Will be updated after metadata extraction
    )
    db.add(material)
    await db.commit()
    await db.refresh(material)

    # Extract metadata in background (simplified for now)
    # In production, this would be a background task
    material.status = "ready"
    await db.commit()

    return MaterialResponse(
        id=str(material.id),
        type=material.type,
        filename=material.filename,
        file_size_bytes=material.file_size_bytes,
        mime_type=material.mime_type,
        storage_path=material.storage_path,
        cdn_url=material.cdn_url,
        duration_ms=material.duration_ms,
        width=material.width,
        height=material.height,
        status=material.status,
    )


@router.get("/{material_id}", response_model=MaterialResponse)
async def get_material(
    workspace_id: UUID,
    material_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(
        select(Material)
        .where(Material.id == material_id)
        .where(Material.workspace_id == workspace_id)
    )
    material = result.scalar_one_or_none()

    if not material:
        raise NotFoundException("Material not found")

    return MaterialResponse(
        id=str(material.id),
        type=material.type,
        filename=material.filename,
        file_size_bytes=material.file_size_bytes,
        mime_type=material.mime_type,
        storage_path=material.storage_path,
        cdn_url=material.cdn_url,
        duration_ms=material.duration_ms,
        width=material.width,
        height=material.height,
        status=material.status,
    )


@router.delete("/{material_id}")
async def delete_material(
    workspace_id: UUID,
    material_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(
        select(Material)
        .where(Material.id == material_id)
        .where(Material.workspace_id == workspace_id)
    )
    material = result.scalar_one_or_none()

    if not material:
        raise NotFoundException("Material not found")

    # Delete from MinIO
    try:
        await storage_service.delete_file(material.storage_path)
    except Exception:
        pass  # Continue even if file deletion fails

    await db.delete(material)
    await db.commit()

    return {"message": "Material deleted"}


@router.get("/{material_id}/download")
async def download_material(
    workspace_id: UUID,
    material_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(
        select(Material)
        .where(Material.id == material_id)
        .where(Material.workspace_id == workspace_id)
    )
    material = result.scalar_one_or_none()

    if not material:
        raise NotFoundException("Material not found")

    # Get presigned URL or file content
    url = await storage_service.get_presigned_url(material.storage_path)
    return {"url": url, "filename": material.original_filename}
