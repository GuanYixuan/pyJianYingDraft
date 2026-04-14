from typing import Optional
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from app.models.order import Order
from app.models.user import User


class OrderService:
    """Service for order operations"""

    @staticmethod
    async def get_order_by_id(db: AsyncSession, order_id: UUID) -> Optional[Order]:
        """Get order by ID"""
        result = await db.execute(select(Order).where(Order.id == order_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_orders_for_user(
        db: AsyncSession,
        user_id: UUID,
        workspace_id: Optional[UUID] = None,
        status: Optional[str] = None,
    ) -> list[Order]:
        """Get orders for a user"""
        query = select(Order).where(Order.user_id == user_id)

        if workspace_id:
            query = query.where(Order.workspace_id == workspace_id)

        if status:
            query = query.where(Order.status == status)

        query = query.order_by(Order.created_at.desc())
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def get_orders_for_operator(
        db: AsyncSession,
        operator_id: UUID,
        status: Optional[str] = None,
    ) -> list[Order]:
        """Get orders assigned to an operator"""
        query = select(Order).where(Order.assigned_operator_id == operator_id)

        if status:
            query = query.where(Order.status == status)

        query = query.order_by(Order.created_at.desc())
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def update_order_status(
        db: AsyncSession,
        order_id: UUID,
        new_status: str,
    ) -> Optional[Order]:
        """Update order status"""
        order = await OrderService.get_order_by_id(db, order_id)
        if not order:
            return None

        order.status = new_status
        await db.commit()
        await db.refresh(order)
        return order

    @staticmethod
    async def assign_operator(
        db: AsyncSession,
        order_id: UUID,
        operator_id: UUID,
    ) -> Optional[Order]:
        """Assign an operator to an order"""
        order = await OrderService.get_order_by_id(db, order_id)
        if not order:
            return None

        order.assigned_operator_id = operator_id
        order.status = "assigned"
        await db.commit()
        await db.refresh(order)
        return order

    @staticmethod
    async def update_ai_script(
        db: AsyncSession,
        order_id: UUID,
        ai_script: str,
    ) -> Optional[Order]:
        """Update AI-generated script for an order"""
        order = await OrderService.get_order_by_id(db, order_id)
        if not order:
            return None

        order.ai_script = ai_script
        await db.commit()
        await db.refresh(order)
        return order

    @staticmethod
    async def get_available_operators(db: AsyncSession) -> list[User]:
        """Get all users with operator role"""
        result = await db.execute(
            select(User).where(User.role.in_(["operator", "admin"]))
        )
        return list(result.scalars().all())

    @staticmethod
    async def get_order_statistics(db: AsyncSession, user_id: UUID = None) -> dict:
        """Get order statistics"""
        query = select(Order)
        if user_id:
            query = query.where(Order.user_id == user_id)

        result = await db.execute(query)
        orders = result.scalars().all()

        stats = {
            "total": len(orders),
            "pending": 0,
            "assigned": 0,
            "processing": 0,
            "completed": 0,
            "failed": 0,
        }

        for order in orders:
            if order.status in stats:
                stats[order.status] += 1

        return stats
