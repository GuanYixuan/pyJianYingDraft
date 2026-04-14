from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

from app.db.database import get_db
from app.models.user import User
from app.models.final_video import FinalVideo
from app.models.order import Order
from app.api.v1.auth import get_current_user
from app.api.v1.workspaces import get_workspace_and_check_access
from app.core.exceptions import NotFoundException, ForbiddenException
from app.services.storage_service import StorageService

router = APIRouter()


class FinalVideoResponse(BaseModel):
    id: str
    order_id: str
    user_id: str
    workspace_id: str
    filename: str
    storage_path: str
    duration_ms: Optional[int]
    thumbnail_url: Optional[str]
    file_size_bytes: Optional[int]
    source_draft_id: Optional[str]
    publish_status: dict
    created_at: datetime

    class Config:
        from_attributes = True


class FinalVideoDetailResponse(FinalVideoResponse):
    order_requirements: Optional[str]
    order_industry: Optional[str]
    order_product: Optional[str]
    order_region: Optional[str]


@router.get("/workspaces/{workspace_id}/final-videos", response_model=list[FinalVideoResponse])
async def list_final_videos(
    workspace_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
    order_id: Optional[UUID] = None,
):
    """List final videos in a workspace"""
    # Verify workspace access
    await get_workspace_and_check_access(workspace_id, db, current_user)

    query = select(FinalVideo).where(FinalVideo.workspace_id == workspace_id)

    if order_id:
        query = query.where(FinalVideo.order_id == order_id)

    # Non-admins can only see their own videos
    result = await db.execute(
        select(FinalVideo)
        .where(FinalVideo.workspace_id == workspace_id)
        .order_by(FinalVideo.created_at.desc())
    )
    videos = result.scalars().all()

    # Filter for non-admins
    if current_user.role == "user":
        videos = [v for v in videos if v.user_id == current_user.id]

    return [
        FinalVideoResponse(
            id=str(v.id),
            order_id=str(v.order_id),
            user_id=str(v.user_id),
            workspace_id=str(v.workspace_id),
            filename=v.filename,
            storage_path=v.storage_path,
            duration_ms=v.duration_ms,
            thumbnail_url=v.thumbnail_url,
            file_size_bytes=v.file_size_bytes,
            source_draft_id=str(v.source_draft_id) if v.source_draft_id else None,
            publish_status=v.publish_status or {},
            created_at=v.created_at,
        )
        for v in videos
    ]


@router.get("/workspaces/{workspace_id}/final-videos/{video_id}", response_model=FinalVideoDetailResponse)
async def get_final_video(
    workspace_id: UUID,
    video_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get final video details"""
    await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(select(FinalVideo).where(FinalVideo.id == video_id))
    video = result.scalar_one_or_none()

    if not video:
        raise NotFoundException("Final video not found")

    if video.workspace_id != workspace_id:
        raise NotFoundException("Final video not found in this workspace")

    if current_user.role == "user" and video.user_id != current_user.id:
        raise ForbiddenException("You don't have access to this video")

    # Get order details
    order_result = await db.execute(select(Order).where(Order.id == video.order_id))
    order = order_result.scalar_one_or_none()

    return FinalVideoDetailResponse(
        id=str(video.id),
        order_id=str(video.order_id),
        user_id=str(video.user_id),
        workspace_id=str(video.workspace_id),
        filename=video.filename,
        storage_path=video.storage_path,
        duration_ms=video.duration_ms,
        thumbnail_url=video.thumbnail_url,
        file_size_bytes=video.file_size_bytes,
        source_draft_id=str(video.source_draft_id) if video.source_draft_id else None,
        publish_status=video.publish_status or {},
        created_at=video.created_at,
        order_requirements=order.requirements if order else None,
        order_industry=order.industry if order else None,
        order_product=order.product if order else None,
        order_region=order.region if order else None,
    )


@router.get("/final-videos/{video_id}/download")
async def get_download_url(
    video_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get presigned download URL for a final video"""
    result = await db.execute(select(FinalVideo).where(FinalVideo.id == video_id))
    video = result.scalar_one_or_none()

    if not video:
        raise NotFoundException("Final video not found")

    if current_user.role == "user" and video.user_id != current_user.id:
        raise ForbiddenException("You don't have access to this video")

    storage = StorageService()
    download_url = storage.get_presigned_url(video.storage_path)

    return {
        "download_url": download_url,
        "filename": video.filename,
        "expires_in": 3600,  # 1 hour
    }


@router.delete("/final-videos/{video_id}")
async def delete_final_video(
    video_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Delete a final video (admin only)"""
    if current_user.role != "admin":
        raise ForbiddenException("Only admins can delete final videos")

    result = await db.execute(select(FinalVideo).where(FinalVideo.id == video_id))
    video = result.scalar_one_or_none()

    if not video:
        raise NotFoundException("Final video not found")

    # Delete from storage
    storage = StorageService()
    try:
        storage.delete_file(video.storage_path)
    except Exception:
        pass  # Ignore storage errors

    # Delete record
    await db.delete(video)
    await db.commit()

    return {"success": True}
