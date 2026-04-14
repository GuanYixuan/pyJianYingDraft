from typing import Optional
from uuid import UUID
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.final_video import FinalVideo
from app.models.publish_record import PublishRecord


class PublishService:
    """Service for publishing operations"""

    @staticmethod
    async def create_publish_record(
        db: AsyncSession,
        final_video_id: UUID,
        platform: str,
    ) -> PublishRecord:
        """Create a new publish record"""
        record = PublishRecord(
            final_video_id=final_video_id,
            platform=platform,
            status="pending",
        )
        db.add(record)
        await db.commit()
        await db.refresh(record)
        return record

    @staticmethod
    async def get_record_by_id(db: AsyncSession, record_id: UUID) -> Optional[PublishRecord]:
        """Get publish record by ID"""
        result = await db.execute(select(PublishRecord).where(PublishRecord.id == record_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_records_for_video(db: AsyncSession, video_id: UUID) -> list[PublishRecord]:
        """Get all publish records for a video"""
        result = await db.execute(
            select(PublishRecord)
            .where(PublishRecord.final_video_id == video_id)
            .order_by(PublishRecord.created_at.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def update_record_success(
        db: AsyncSession,
        record_id: UUID,
        external_video_id: str,
        external_url: str,
    ) -> Optional[PublishRecord]:
        """Mark publish record as successful"""
        record = await PublishService.get_record_by_id(db, record_id)
        if not record:
            return None

        record.status = "success"
        record.external_video_id = external_video_id
        record.external_url = external_url
        record.published_at = datetime.utcnow()

        await db.commit()
        await db.refresh(record)
        return record

    @staticmethod
    async def update_record_failed(
        db: AsyncSession,
        record_id: UUID,
        error_message: str,
    ) -> Optional[PublishRecord]:
        """Mark publish record as failed"""
        record = await PublishService.get_record_by_id(db, record_id)
        if not record:
            return None

        record.status = "failed"
        record.error_message = error_message

        await db.commit()
        await db.refresh(record)
        return record

    @staticmethod
    async def get_existing_record(
        db: AsyncSession,
        video_id: UUID,
        platform: str,
    ) -> Optional[PublishRecord]:
        """Check if video already published to a platform"""
        result = await db.execute(
            select(PublishRecord)
            .where(PublishRecord.final_video_id == video_id)
            .where(PublishRecord.platform == platform)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def is_published_to_platform(
        db: AsyncSession,
        video_id: UUID,
        platform: str,
    ) -> bool:
        """Check if video is successfully published to a platform"""
        record = await PublishService.get_existing_record(db, video_id, platform)
        return record is not None and record.status == "success"

    @staticmethod
    async def get_publish_status_summary(
        db: AsyncSession,
        video_id: UUID,
    ) -> dict:
        """Get publish status summary for all platforms"""
        records = await PublishService.get_records_for_video(db, video_id)

        summary = {
            "douyin": {"published": False, "video_id": None, "url": None, "last_attempt": None},
            "wechat_channels": {"published": False, "video_id": None, "url": None, "last_attempt": None},
        }

        for record in records:
            if record.platform in summary:
                summary[record.platform] = {
                    "published": record.status == "success",
                    "video_id": record.external_video_id,
                    "url": record.external_url,
                    "last_attempt": record.created_at.isoformat() if record.created_at else None,
                    "status": record.status,
                }

        return summary
