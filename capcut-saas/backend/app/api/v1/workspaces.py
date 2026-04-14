from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

from app.db.database import get_db
from app.models.workspace import Workspace, WorkspaceMember, Tenant
from app.models.user import User
from app.api.v1.auth import get_current_user
from app.core.exceptions import NotFoundException, ForbiddenException

router = APIRouter()


class WorkspaceCreate(BaseModel):
    name: str
    description: Optional[str] = None
    tenant_name: Optional[str] = None


class WorkspaceResponse(BaseModel):
    id: str
    name: str
    description: Optional[str]
    role: str  # current user's role in this workspace

    class Config:
        from_attributes = True


class WorkspaceMemberResponse(BaseModel):
    user_id: str
    email: str
    full_name: Optional[str]
    role: str

    class Config:
        from_attributes = True


async def get_workspace_and_check_access(
    workspace_id: UUID,
    db: AsyncSession,
    user: User,
    require_role: Optional[str] = None,
) -> tuple[Workspace, WorkspaceMember]:
    # Find workspace member entry
    result = await db.execute(
        select(WorkspaceMember)
        .where(WorkspaceMember.workspace_id == workspace_id)
        .where(WorkspaceMember.user_id == user.id)
    )
    membership = result.scalar_one_or_none()

    if not membership:
        raise ForbiddenException("You are not a member of this workspace")

    if require_role and membership.role not in require_role:
        raise ForbiddenException(f"Requires role: {require_role}")

    result = await db.execute(select(Workspace).where(Workspace.id == workspace_id))
    workspace = result.scalar_one_or_none()

    if not workspace:
        raise NotFoundException("Workspace not found")

    return workspace, membership


@router.get("", response_model=list[WorkspaceResponse])
async def list_workspaces(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(Workspace)
        .join(WorkspaceMember)
        .where(WorkspaceMember.user_id == current_user.id)
    )
    workspaces = result.scalars().all()

    response = []
    for ws in workspaces:
        # Get current user's role in this workspace
        member_result = await db.execute(
            select(WorkspaceMember)
            .where(WorkspaceMember.workspace_id == ws.id)
            .where(WorkspaceMember.user_id == current_user.id)
        )
        membership = member_result.scalar_one()
        response.append(
            WorkspaceResponse(
                id=str(ws.id),
                name=ws.name,
                description=ws.description,
                role=membership.role,
            )
        )
    return response


@router.post("", response_model=WorkspaceResponse)
async def create_workspace(
    data: WorkspaceCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Create or get tenant
    if data.tenant_name:
        tenant = Tenant(name=data.tenant_name, slug=data.tenant_name.lower().replace(" ", "-"))
        db.add(tenant)
        await db.flush()
    else:
        # Use a default tenant for now
        result = await db.execute(select(Tenant).limit(1))
        tenant = result.scalar_one_or_none()
        if not tenant:
            tenant = Tenant(name="Default", slug="default")
            db.add(tenant)
            await db.flush()

    # Create workspace
    workspace = Workspace(
        tenant_id=tenant.id,
        name=data.name,
        description=data.description,
    )
    db.add(workspace)
    await db.flush()

    # Add current user as admin
    membership = WorkspaceMember(
        workspace_id=workspace.id,
        user_id=current_user.id,
        role="admin",
    )
    db.add(membership)
    await db.commit()
    await db.refresh(workspace)

    return WorkspaceResponse(
        id=str(workspace.id),
        name=workspace.name,
        description=workspace.description,
        role="admin",
    )


@router.get("/{workspace_id}", response_model=WorkspaceResponse)
async def get_workspace(
    workspace_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    workspace, membership = await get_workspace_and_check_access(
        workspace_id, db, current_user
    )
    return WorkspaceResponse(
        id=str(workspace.id),
        name=workspace.name,
        description=workspace.description,
        role=membership.role,
    )


@router.get("/{workspace_id}/members", response_model=list[WorkspaceMemberResponse])
async def list_members(
    workspace_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    workspace, _ = await get_workspace_and_check_access(workspace_id, db, current_user)

    result = await db.execute(
        select(WorkspaceMember)
        .options(selectinload(WorkspaceMember.user))
        .where(WorkspaceMember.workspace_id == workspace_id)
    )
    members = result.scalars().all()

    return [
        WorkspaceMemberResponse(
            user_id=str(m.user_id),
            email=m.user.email,
            full_name=m.user.full_name,
            role=m.role,
        )
        for m in members
    ]
