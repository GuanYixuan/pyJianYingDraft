from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.draft import Draft
from app.models.template import Template
from app.models.material import Material
from app.draft_engine.generator import DraftGenerator
from uuid import UUID


class DraftService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.generator = DraftGenerator()

    async def generate_from_template(
        self,
        template: Template,
        project_id: UUID,
        materials_mapping: dict,
        text_replacements: dict,
        options: dict,
        user_id: UUID,
    ) -> Draft:
        """Generate a draft from template using pyJianYingDraft"""

        # Get material storage paths
        material_paths = {}
        for template_name, material_uuid in materials_mapping.items():
            result = await self.db.execute(
                select(Material).where(Material.id == material_uuid)
            )
            material = result.scalar_one_or_none()
            if material:
                material_paths[template_name] = {
                    "id": str(material.id),
                    "path": material.storage_path,
                    "type": material.type,
                    "filename": material.filename,
                }

        # Generate draft content
        generated_content = self.generator.generate(
            template_content=template.content,
            materials_mapping=material_paths,
            text_replacements=text_replacements,
            output_settings=options,
        )

        # Create draft record
        draft = Draft(
            project_id=project_id,
            workspace_id=template.workspace_id,
            name=f"Generated from {template.name}",
            content=generated_content,
            source_template_id=template.id,
            metadata=template.metadata,
            created_by=user_id,
        )
        self.db.add(draft)

        # Update template usage count
        template.usage_count += 1

        await self.db.commit()
        await self.db.refresh(draft)

        return draft
