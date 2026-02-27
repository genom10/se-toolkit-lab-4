"""Database operations for interactions."""
from datetime import datetime

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.interaction import InteractionLog


async def read_interactions(session: AsyncSession) -> list[InteractionLog]:
    """Read all interactions from the database."""
    result = await session.exec(select(InteractionLog))
    return list(result.all())


async def insert_interaction(
        session: AsyncSession, 
        learner_id: int,
        item_id: int,
        kind: str
) -> InteractionLog:
    """Create an interaction"""
    instance = InteractionLog(
        learner_id=learner_id,
        item_id=item_id,
        kind=kind,
        created_at=datetime.now()    
    )
    session.add(instance)

    await session.commit()
    await session.refresh(instance)
    
    return instance

