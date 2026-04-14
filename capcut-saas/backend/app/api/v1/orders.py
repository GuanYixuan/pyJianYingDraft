from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from pydantic import BaseModel
from typing import Optional
from uuid import UUID, UUID4
from datetime import datetime

from app.db.database import get_db
from app.models.user import User
from app.models.order import Order
from app.models.material import Material
from app.api.v1.auth import get_current_user
from app.api.v1.workspaces import get_workspace_and_check_access
from app.core.exceptions import NotFoundException, ForbiddenException, BadRequestException

router = APIRouter()


class OrderCreate(BaseModel):
    workspace_id: UUID
    requirements: Optional[str] = None
    industry: Optional[str] = None
    product: Optional[str] = None
    region: Optional[str] = None
    material_ids: list[UUID4] = []
    priority: str = "normal"


class OrderResponse(BaseModel):
    id: str
    user_id: str
    workspace_id: str
    requirements: Optional[str]
    industry: Optional[str]
    product: Optional[str]
    region: Optional[str]
    material_ids: list[str]
    assigned_operator_id: Optional[str]
    status: str
    priority: str
    ai_script: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class OrderUpdateStatus(BaseModel):
    status: str  # pending/assigned/processing/completed/failed


class OrderAssign(BaseModel):
    operator_id: UUID4


@router.get("", response_model=list[OrderResponse])
async def list_orders(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
    workspace_id: Optional[UUID] = None,
    status_filter: Optional[str] = None,
):
    """List orders for current user (or all if operator/admin)"""
    query = select(Order)

    # Non-operators can only see their own orders
    if current_user.role == "user":
        query = query.where(Order.user_id == current_user.id)

    if workspace_id:
        query = query.where(Order.workspace_id == workspace_id)

    if status_filter:
        query = query.where(Order.status == status_filter)

    query = query.order_by(Order.created_at.desc())
    result = await db.execute(query)
    orders = result.scalars().all()

    return [
        OrderResponse(
            id=str(o.id),
            user_id=str(o.user_id),
            workspace_id=str(o.workspace_id),
            requirements=o.requirements,
            industry=o.industry,
            product=o.product,
            region=o.region,
            material_ids=[str(m) for m in (o.material_ids or [])],
            assigned_operator_id=str(o.assigned_operator_id) if o.assigned_operator_id else None,
            status=o.status,
            priority=o.priority,
            ai_script=o.ai_script,
            created_at=o.created_at,
        )
        for o in orders
    ]


@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(
    data: OrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a new order"""
    # Verify workspace access
    await get_workspace_and_check_access(data.workspace_id, db, current_user)

    order = Order(
        user_id=current_user.id,
        workspace_id=data.workspace_id,
        requirements=data.requirements,
        industry=data.industry or current_user.industry,
        product=data.product or current_user.product,
        region=data.region or current_user.region,
        material_ids=data.material_ids,
        priority=data.priority,
        status="pending",
    )
    db.add(order)
    await db.commit()
    await db.refresh(order)

    return OrderResponse(
        id=str(order.id),
        user_id=str(order.user_id),
        workspace_id=str(order.workspace_id),
        requirements=order.requirements,
        industry=order.industry,
        product=order.product,
        region=order.region,
        material_ids=[str(m) for m in (order.material_ids or [])],
        assigned_operator_id=None,
        status=order.status,
        priority=order.priority,
        ai_script=None,
        created_at=order.created_at,
    )


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(
    order_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get order details"""
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()

    if not order:
        raise NotFoundException("Order not found")

    # Users can only view their own orders
    if current_user.role == "user" and order.user_id != current_user.id:
        raise ForbiddenException("You don't have access to this order")

    return OrderResponse(
        id=str(order.id),
        user_id=str(order.user_id),
        workspace_id=str(order.workspace_id),
        requirements=order.requirements,
        industry=order.industry,
        product=order.product,
        region=order.region,
        material_ids=[str(m) for m in (order.material_ids or [])],
        assigned_operator_id=str(order.assigned_operator_id) if order.assigned_operator_id else None,
        status=order.status,
        priority=order.priority,
        ai_script=order.ai_script,
        created_at=order.created_at,
    )


@router.patch("/{order_id}/status", response_model=OrderResponse)
async def update_order_status(
    order_id: UUID,
    data: OrderUpdateStatus,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update order status (operator only)"""
    if current_user.role not in ("operator", "admin"):
        raise ForbiddenException("Only operators can update order status")

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()

    if not order:
        raise NotFoundException("Order not found")

    valid_statuses = ("pending", "assigned", "processing", "completed", "failed")
    if data.status not in valid_statuses:
        raise BadRequestException(f"Invalid status. Must be one of: {valid_statuses}")

    order.status = data.status
    await db.commit()
    await db.refresh(order)

    return OrderResponse(
        id=str(order.id),
        user_id=str(order.user_id),
        workspace_id=str(order.workspace_id),
        requirements=order.requirements,
        industry=order.industry,
        product=order.product,
        region=order.region,
        material_ids=[str(m) for m in (order.material_ids or [])],
        assigned_operator_id=str(order.assigned_operator_id) if order.assigned_operator_id else None,
        status=order.status,
        priority=order.priority,
        ai_script=order.ai_script,
        created_at=order.created_at,
    )


@router.post("/{order_id}/assign", response_model=OrderResponse)
async def assign_operator(
    order_id: UUID,
    data: OrderAssign,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Assign an operator to the order (admin only)"""
    if current_user.role != "admin":
        raise ForbiddenException("Only admins can assign operators")

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()

    if not order:
        raise NotFoundException("Order not found")

    # Verify operator exists and has operator role
    op_result = await db.execute(select(User).where(User.id == data.operator_id))
    operator = op_result.scalar_one_or_none()

    if not operator:
        raise NotFoundException("Operator not found")

    if operator.role not in ("operator", "admin"):
        raise BadRequestException("指定的员工不是操作员")

    order.assigned_operator_id = data.operator_id
    order.status = "assigned"
    await db.commit()
    await db.refresh(order)

    return OrderResponse(
        id=str(order.id),
        user_id=str(order.user_id),
        workspace_id=str(order.workspace_id),
        requirements=order.requirements,
        industry=order.industry,
        product=order.product,
        region=order.region,
        material_ids=[str(m) for m in (order.material_ids or [])],
        assigned_operator_id=str(order.assigned_operator_id) if order.assigned_operator_id else None,
        status=order.status,
        priority=order.priority,
        ai_script=order.ai_script,
        created_at=order.created_at,
    )


@router.get("/{order_id}/materials")
async def get_order_materials(
    order_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get materials associated with an order (for operator download)"""
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()

    if not order:
        raise NotFoundException("Order not found")

    # Check access
    if current_user.role == "user" and order.user_id != current_user.id:
        raise ForbiddenException("You don't have access to this order")

    if not order.material_ids:
        return []

    mat_result = await db.execute(
        select(Material).where(Material.id.in_(order.material_ids))
    )
    materials = mat_result.scalars().all()

    return [
        {
            "id": str(m.id),
            "filename": m.filename,
            "type": m.type,
            "file_size_bytes": m.file_size_bytes,
            "cdn_url": m.cdn_url,
        }
        for m in materials
    ]
