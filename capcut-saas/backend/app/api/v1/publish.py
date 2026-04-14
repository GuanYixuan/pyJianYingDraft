from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

from app.db.database import get_db
from app.models.user import User
from app.models.final_video import FinalVideo
from app.models.publish_record import PublishRecord
from app.api.v1.auth import get_current_user
from app.core.exceptions import NotFoundException, ForbiddenException, BadRequestException

router = APIRouter()


class PublishResponse(BaseModel):
    id: str
    final_video_id: str
    platform: str
    external_video_id: Optional[str]
    external_url: Optional[str]
    status: str
    published_at: Optional[datetime]

    class Config:
        from_attributes = True


class PublishStatusResponse(BaseModel):
    douyin: dict
    wechat_channels: dict


async def publish_to_douyin(final_video: FinalVideo, db: AsyncSession) -> PublishRecord:
    """Publish video to Douyin (placeholder - needs real API integration)"""
    # TODO: Implement actual Douyin API integration
    # This would use the integrations/douyin/ module

    record = PublishRecord(
        final_video_id=final_video.id,
        platform="douyin",
        status="pending",
    )
    db.add(record)
    await db.commit()
    await db.refresh(record)

    return record


async def publish_to_wechat_channels(final_video: FinalVideo, db: AsyncSession) -> PublishRecord:
    """Publish video to WeChat Channels (placeholder - needs real API integration)"""
    # TODO: Implement actual WeChat Channels API integration
    # This would use the integrations/wechat_channels/ module

    record = PublishRecord(
        final_video_id=final_video.id,
        platform="wechat_channels",
        status="pending",
    )
    db.add(record)
    await db.commit()
    await db.refresh(record)

    return record


@router.post("/final-videos/{video_id}/publish/douyin", response_model=PublishResponse)
async def publish_to_douyin_endpoint(
    video_id: UUID,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Publish final video to Douyin"""
    result = await db.execute(select(FinalVideo).where(FinalVideo.id == video_id))
    final_video = result.scalar_one_or_none()

    if not final_video:
        raise NotFoundException("Final video not found")

    if current_user.role == "user" and final_video.user_id != current_user.id:
        raise ForbiddenException("You don't have access to this video")

    # Check if already published
    pub_result = await db.execute(
        select(PublishRecord)
        .where(PublishRecord.final_video_id == video_id)
        .where(PublishRecord.platform == "douyin")
    )
    existing = pub_result.scalar_one_or_none()

    if existing and existing.status == "success":
        raise BadRequestException("Video already published to Douyin")

    # Create or update publish record
    if existing:
        record = existing
        record.status = "pending"
        record.published_at = None
    else:
        record = PublishRecord(
            final_video_id=video_id,
            platform="douyin",
            status="pending",
        )
        db.add(record)

    # Update publish status in final_video
    if not final_video.publish_status:
        final_video.publish_status = {}
    final_video.publish_status["douyin"] = {
        "published": False,
        "pending": True,
    }

    await db.commit()
    await db.refresh(record)

    # TODO: Trigger actual publishing in background task
    # For now, mark as success after a delay (placeholder)
    # background_tasks.add_task(publish_to_douyin, final_video, db)

    return PublishResponse(
        id=str(record.id),
        final_video_id=str(record.final_video_id),
        platform=record.platform,
        external_video_id=record.external_video_id,
        external_url=record.external_url,
        status=record.status,
        published_at=record.published_at,
    )


@router.post("/final-videos/{video_id}/publish/wechat-channels", response_model=PublishResponse)
async def publish_to_wechat_channels_endpoint(
    video_id: UUID,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Publish final video to WeChat Channels"""
    result = await db.execute(select(FinalVideo).where(FinalVideo.id == video_id))
    final_video = result.scalar_one_or_none()

    if not final_video:
        raise NotFoundException("Final video not found")

    if current_user.role == "user" and final_video.user_id != current_user.id:
        raise ForbiddenException("You don't have access to this video")

    # Check if already published
    pub_result = await db.execute(
        select(PublishRecord)
        .where(PublishRecord.final_video_id == video_id)
        .where(PublishRecord.platform == "wechat_channels")
    )
    existing = pub_result.scalar_one_or_none()

    if existing and existing.status == "success":
        raise BadRequestException("Video already published to WeChat Channels")

    # Create or update publish record
    if existing:
        record = existing
        record.status = "pending"
        record.published_at = None
    else:
        record = PublishRecord(
            final_video_id=video_id,
            platform="wechat_channels",
            status="pending",
        )
        db.add(record)

    # Update publish status in final_video
    if not final_video.publish_status:
        final_video.publish_status = {}
    final_video.publish_status["wechat_channels"] = {
        "published": False,
        "pending": True,
    }

    await db.commit()
    await db.refresh(record)

    # TODO: Trigger actual publishing in background task

    return PublishResponse(
        id=str(record.id),
        final_video_id=str(record.final_video_id),
        platform=record.platform,
        external_video_id=record.external_video_id,
        external_url=record.external_url,
        status=record.status,
        published_at=record.published_at,
    )


@router.get("/final-videos/{video_id}/publish-status", response_model=PublishStatusResponse)
async def get_publish_status(
    video_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get publishing status for all platforms"""
    result = await db.execute(select(FinalVideo).where(FinalVideo.id == video_id))
    final_video = result.scalar_one_or_none()

    if not final_video:
        raise NotFoundException("Final video not found")

    if current_user.role == "user" and final_video.user_id != current_user.id:
        raise ForbiddenException("You don't have access to this video")

    # Get all publish records
    pub_result = await db.execute(
        select(PublishRecord).where(PublishRecord.final_video_id == video_id)
    )
    records = pub_result.scalars().all()

    status = {
        "douyin": {"published": False, "video_id": None, "url": None},
        "wechat_channels": {"published": False, "video_id": None, "url": None},
    }

    for record in records:
        if record.platform == "douyin":
            status["douyin"] = {
                "published": record.status == "success",
                "video_id": record.external_video_id,
                "url": record.external_url,
            }
        elif record.platform == "wechat_channels":
            status["wechat_channels"] = {
                "published": record.status == "success",
                "video_id": record.external_video_id,
                "url": record.external_url,
            }

    return PublishStatusResponse(**status)


@router.get("/final-videos/{video_id}/publish-history", response_model=list[PublishResponse])
async def get_publish_history(
    video_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get publishing history for a video"""
    result = await db.execute(select(FinalVideo).where(FinalVideo.id == video_id))
    final_video = result.scalar_one_or_none()

    if not final_video:
        raise NotFoundException("Final video not found")

    if current_user.role == "user" and final_video.user_id != current_user.id:
        raise ForbiddenException("You don't have access to this video")

    pub_result = await db.execute(
        select(PublishRecord)
        .where(PublishRecord.final_video_id == video_id)
        .order_by(PublishRecord.created_at.desc())
    )
    records = pub_result.scalars().all()

    return [
        PublishResponse(
            id=str(r.id),
            final_video_id=str(r.final_video_id),
            platform=r.platform,
            external_video_id=r.external_video_id,
            external_url=r.external_url,
            status=r.status,
            published_at=r.published_at,
        )
        for r in records
    ]
