from fastapi import APIRouter, Depends, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import Optional

from app.db.database import get_db
from app.models.project import Project
from app.models.workspace import Workspace, WorkspaceMember
from app.models.user import User
from app.api.v1.auth import get_current_user
from app.api.v1.workspaces import get_workspace_and_check_access
from app.core.exceptions import NotFoundException

router = APIRouter()


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    settings: Optional[dict] = None


class ProjectResponse(BaseModel):
    id: str
    name: str
    description: Optional[str]
    settings: dict

    class Config:
        from_attributes = True


@router.get("", response_model=list[ProjectResponse])
async def list_projects(
    workspace_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(
        select(Project).where(Project.workspace_id == workspace_id)
    )
    projects = result.scalars().all()

    return [
        ProjectResponse(
            id=str(p.id),
            name=p.name,
            description=p.description,
            settings=p.settings or {},
        )
        for p in projects
    ]


@router.post("", response_model=ProjectResponse)
async def create_project(
    workspace_id: UUID,
    data: ProjectCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    project = Project(
        workspace_id=workspace_id,
        name=data.name,
        description=data.description,
        settings=data.settings or {},
        created_by=current_user.id,
    )
    db.add(project)
    await db.commit()
    await db.refresh(project)

    return ProjectResponse(
        id=str(project.id),
        name=project.name,
        description=project.description,
        settings=project.settings or {},
    )


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    workspace_id: UUID,
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(
        select(Project)
        .where(Project.id == project_id)
        .where(Project.workspace_id == workspace_id)
    )
    project = result.scalar_one_or_none()

    if not project:
        raise NotFoundException("Project not found")

    return ProjectResponse(
        id=str(project.id),
        name=project.name,
        description=project.description,
        settings=project.settings or {},
    )
