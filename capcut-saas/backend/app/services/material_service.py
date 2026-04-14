from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.material import Material
from app.models.material_mapping import MaterialMapping
import pymediainfo


class MaterialService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def extract_metadata(self, material: Material, file_path: str) -> dict:
        """Extract video/audio/image metadata using pymediainfo"""
        try:
            media_info = pymediainfo.MediaInfo.parse(file_path)
            track = media_info.tracks[0]

            metadata = {}
            if track.track_type == "Video":
                metadata = {
                    "duration_ms": int(float(track.duration) * 1000) if track.duration else None,
                    "width": track.width,
                    "height": track.height,
                }
            elif track.track_type == "Audio":
                metadata = {
                    "duration_ms": int(float(track.duration) * 1000) if track.duration else None,
                }
            elif track.track_type == "Image":
                metadata = {
                    "width": track.width,
                    "height": track.height,
                }

            return metadata
        except Exception as e:
            print(f"Error extracting metadata: {e}")
            return {}

    async def update_material_metadata(self, material_id: str, metadata: dict):
        material = await self.db.execute(
            select(Material).where(Material.id == material_id)
        )
        material = material.scalar_one_or_none()
        if material:
            for key, value in metadata.items():
                setattr(material, key, value)
            material.status = "ready"
            await self.db.commit()
