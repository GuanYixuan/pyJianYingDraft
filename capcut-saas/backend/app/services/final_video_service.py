from typing import Optional, BinaryIO
from uuid import UUID
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.final_video import FinalVideo
from app.models.order import Order
from app.services.storage_service import StorageService


class FinalVideoService:
    """Service for final video operations"""

    @staticmethod
    async def get_by_id(db: AsyncSession, video_id: UUID) -> Optional[FinalVideo]:
        """Get final video by ID"""
        result = await db.execute(select(FinalVideo).where(FinalVideo.id == video_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_order(db: AsyncSession, order_id: UUID) -> list[FinalVideo]:
        """Get all final videos for an order"""
        result = await db.execute(
            select(FinalVideo)
            .where(FinalVideo.order_id == order_id)
            .order_by(FinalVideo.created_at.desc())
        )
        return list(result.scalars().all())

    @staticmethod
    async def get_by_workspace(
        db: AsyncSession,
        workspace_id: UUID,
        user_id: Optional[UUID] = None,
    ) -> list[FinalVideo]:
        """Get all final videos in a workspace"""
        query = select(FinalVideo).where(FinalVideo.workspace_id == workspace_id)

        if user_id:
            query = query.where(FinalVideo.user_id == user_id)

        query = query.order_by(FinalVideo.created_at.desc())
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def create(
        db: AsyncSession,
        order_id: UUID,
        user_id: UUID,
        workspace_id: UUID,
        filename: str,
        storage_path: str,
        file_size_bytes: int,
        duration_ms: Optional[int] = None,
        thumbnail_url: Optional[str] = None,
        source_draft_id: Optional[UUID] = None,
    ) -> FinalVideo:
        """Create a new final video record"""
        video = FinalVideo(
            order_id=order_id,
            user_id=user_id,
            workspace_id=workspace_id,
            filename=filename,
            storage_path=storage_path,
            file_size_bytes=file_size_bytes,
            duration_ms=duration_ms,
            thumbnail_url=thumbnail_url,
            source_draft_id=source_draft_id,
            publish_status={
                "douyin": {"published": False},
                "wechat_channels": {"published": False},
            },
        )
        db.add(video)
        await db.commit()
        await db.refresh(video)
        return video

    @staticmethod
    async def upload_video(
        db: AsyncSession,
        order_id: UUID,
        user_id: UUID,
        workspace_id: UUID,
        file: BinaryIO,
        filename: str,
        content_type: str,
    ) -> FinalVideo:
        """Upload and create final video"""
        storage = StorageService()

        # Generate storage path
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        storage_path = f"final-videos/{order_id}/{timestamp}_{filename}"

        # Upload to storage
        storage.upload_file(file.read(), storage_path, content_type)

        # Get file size
        file.seek(0, 2)  # Seek to end
        file_size = file.tell()
        file.seek(0)  # Reset position

        # Create record
        return await FinalVideoService.create(
            db=db,
            order_id=order_id,
            user_id=user_id,
            workspace_id=workspace_id,
            filename=filename,
            storage_path=storage_path,
            file_size_bytes=file_size,
        )

    @staticmethod
    async def get_download_url(storage_path: str) -> str:
        """Get presigned download URL"""
        storage = StorageService()
        return storage.get_presigned_url(storage_path)

    @staticmethod
    async def update_publish_status(
        db: AsyncSession,
        video_id: UUID,
        platform: str,
        published: bool,
        external_video_id: Optional[str] = None,
        external_url: Optional[str] = None,
    ) -> Optional[FinalVideo]:
        """Update publish status for a platform"""
        video = await FinalVideoService.get_by_id(db, video_id)
        if not video:
            return None

        if not video.publish_status:
            video.publish_status = {}

        video.publish_status[platform] = {
            "published": published,
            "video_id": external_video_id,
            "url": external_url,
        }

        await db.commit()
        await db.refresh(video)
        return video

    @staticmethod
    async def delete(db: AsyncSession, video_id: UUID) -> bool:
        """Delete a final video"""
        video = await FinalVideoService.get_by_id(db, video_id)
        if not video:
            return False

        # Delete from storage
        storage = StorageService()
        try:
            storage.delete_file(video.storage_path)
        except Exception:
            pass

        await db.delete(video)
        await db.commit()
        return True
