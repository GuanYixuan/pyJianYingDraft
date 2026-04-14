from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import Optional
from uuid import UUID, UUID4
from datetime import datetime

from app.db.database import get_db
from app.models.user import User
from app.models.order import Order
from app.models.final_video import FinalVideo
from app.models.draft import Draft
from app.models.material import Material
from app.api.v1.auth import get_current_user
from app.core.exceptions import NotFoundException, ForbiddenException, BadRequestException
from app.services.storage_service import StorageService

router = APIRouter()


class OrderDetailResponse(BaseModel):
    id: str
    user_id: str
    workspace_id: str
    requirements: Optional[str]
    industry: Optional[str]
    product: Optional[str]
    region: Optional[str]
    material_ids: list[str]
    status: str
    priority: str
    ai_script: Optional[str]
    created_at: datetime
    user_email: Optional[str]
    user_full_name: Optional[str]

    class Config:
        from_attributes = True


class FinalVideoCreate(BaseModel):
    order_id: UUID4
    filename: str
    storage_path: str
    duration_ms: Optional[int] = None
    thumbnail_url: Optional[str] = None
    file_size_bytes: Optional[int] = None
    source_draft_id: Optional[UUID4] = None


@router.get("/orders", response_model=list[OrderDetailResponse])
async def list_operator_orders(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
    status_filter: Optional[str] = None,
):
    """List orders assigned to or available for the operator"""
    if current_user.role not in ("operator", "admin"):
        raise ForbiddenException("Only operators can access this endpoint")

    query = select(Order)

    # Operators see assigned orders, admins see all
    if current_user.role == "operator":
        query = query.where(Order.assigned_operator_id == current_user.id)

    if status_filter:
        query = query.where(Order.status == status_filter)

    query = query.order_by(Order.created_at.desc())
    result = await db.execute(query.options(selectinload(Order.user)))
    orders = result.scalars().all()

    return [
        OrderDetailResponse(
            id=str(o.id),
            user_id=str(o.user_id),
            workspace_id=str(o.workspace_id),
            requirements=o.requirements,
            industry=o.industry,
            product=o.product,
            region=o.region,
            material_ids=[str(m) for m in (o.material_ids or [])],
            status=o.status,
            priority=o.priority,
            ai_script=o.ai_script,
            created_at=o.created_at,
            user_email=o.user.email if o.user else None,
            user_full_name=o.user.full_name if o.user else None,
        )
        for o in orders
    ]


@router.get("/orders/{order_id}", response_model=OrderDetailResponse)
async def get_operator_order(
    order_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get detailed order info for operator"""
    if current_user.role not in ("operator", "admin"):
        raise ForbiddenException("Only operators can access this endpoint")

    result = await db.execute(
        select(Order)
        .options(selectinload(Order.user))
        .where(Order.id == order_id)
    )
    order = result.scalar_one_or_none()

    if not order:
        raise NotFoundException("Order not found")

    # Operators can only see their assigned orders
    if current_user.role == "operator" and order.assigned_operator_id != current_user.id:
        raise ForbiddenException("This order is not assigned to you")

    return OrderDetailResponse(
        id=str(order.id),
        user_id=str(order.user_id),
        workspace_id=str(order.workspace_id),
        requirements=order.requirements,
        industry=order.industry,
        product=order.product,
        region=order.region,
        material_ids=[str(m) for m in (order.material_ids or [])],
        status=order.status,
        priority=order.priority,
        ai_script=order.ai_script,
        created_at=order.created_at,
        user_email=order.user.email if order.user else None,
        user_full_name=order.user.full_name if order.user else None,
    )


@router.get("/orders/{order_id}/materials")
async def get_order_materials_for_operator(
    order_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get downloadable material links for an order"""
    if current_user.role not in ("operator", "admin"):
        raise ForbiddenException("Only operators can access this endpoint")

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()

    if not order:
        raise NotFoundException("Order not found")

    if current_user.role == "operator" and order.assigned_operator_id != current_user.id:
        raise ForbiddenException("This order is not assigned to you")

    if not order.material_ids:
        return []

    mat_result = await db.execute(
        select(Material).where(Material.id.in_(order.material_ids))
    )
    materials = mat_result.scalars().all()

    storage = StorageService()

    return [
        {
            "id": str(m.id),
            "filename": m.filename,
            "original_filename": m.original_filename,
            "type": m.type,
            "file_size_bytes": m.file_size_bytes,
            "download_url": storage.get_presigned_url(m.storage_path) if m.storage_path else None,
            "cdn_url": m.cdn_url,
        }
        for m in materials
    ]


@router.post("/orders/{order_id}/final-video", response_model=dict)
async def upload_final_video(
    order_id: UUID,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Upload final video for an order"""
    if current_user.role not in ("operator", "admin"):
        raise ForbiddenException("Only operators can upload final videos")

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()

    if not order:
        raise NotFoundException("Order not found")

    if current_user.role == "operator" and order.assigned_operator_id != current_user.id:
        raise ForbiddenException("This order is not assigned to you")

    # Validate file type
    allowed_types = ["video/mp4", "video/x-matroska", "video/webm"]
    if file.content_type not in allowed_types:
        raise BadRequestException(f"Invalid file type. Allowed: {allowed_types}")

    # Upload to MinIO
    storage = StorageService()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = file.filename or f"final_{order_id}_{timestamp}.mp4"
    storage_path = f"final-videos/{order_id}/{filename}"

    # Read and upload file
    content = await file.read()
    storage.upload_file(content, storage_path, file.content_type)

    # Create final video record
    final_video = FinalVideo(
        order_id=order_id,
        user_id=order.user_id,
        workspace_id=order.workspace_id,
        filename=filename,
        storage_path=storage_path,
        file_size_bytes=len(content),
    )
    db.add(final_video)

    # Update order status
    order.status = "completed"

    await db.commit()
    await db.refresh(final_video)

    return {
        "id": str(final_video.id),
        "filename": final_video.filename,
        "storage_path": final_video.storage_path,
        "file_size_bytes": final_video.file_size_bytes,
        "created_at": final_video.created_at.isoformat(),
    }


@router.patch("/orders/{order_id}/ai-script", response_model=dict)
async def update_ai_script(
    order_id: UUID,
    script: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update AI-generated script for an order"""
    if current_user.role not in ("operator", "admin"):
        raise ForbiddenException("Only operators can update AI script")

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()

    if not order:
        raise NotFoundException("Order not found")

    if current_user.role == "operator" and order.assigned_operator_id != current_user.id:
        raise ForbiddenException("This order is not assigned to you")

    order.ai_script = script
    await db.commit()

    return {"success": True, "ai_script": script}


@router.patch("/orders/{order_id}/status", response_model=dict)
async def update_order_processing_status(
    order_id: UUID,
    new_status: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update order status (operator shortcut)"""
    if current_user.role not in ("operator", "admin"):
        raise ForbiddenException("Only operators can update order status")

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()

    if not order:
        raise NotFoundException("Order not found")

    if current_user.role == "operator" and order.assigned_operator_id != current_user.id:
        raise ForbiddenException("This order is not assigned to you")

    valid_statuses = ("pending", "assigned", "processing", "completed", "failed")
    if new_status not in valid_statuses:
        raise BadRequestException(f"Invalid status. Must be one of: {valid_statuses}")

    order.status = new_status
    await db.commit()

    return {"success": True, "status": new_status}
