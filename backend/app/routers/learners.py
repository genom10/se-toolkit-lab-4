"""Router for learner endpoints."""

from fastapi import APIRouter

from datetime import datetime

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.learners import read_learners, create_learner
from app.models.learner import Learner, LearnerCreate

router = APIRouter()

# ===
# PART A: GET endpoint
# ===

# UNCOMMENT AND FILL IN

@router.get("/", response_model=list[Learner])
async def get_learners(
    body: Learner | None = None,
    session: AsyncSession = Depends(get_session),
):
    """ Obtain learners """
    return await read_learners(session, body.enrolled_at)

# Reference:
# items GET -> reads from items table, returns list[Item]
# learners GET -> reads from learners table, returns list[Learner]
# Query parameter: ?enrolled_after= filters learners by enrolled_at date

# ===
# PART B: POST endpoint
# ===

# UNCOMMENT AND FILL IN

@router.post("/<resource_name>", response_model=Learner, status_code=201)
async def create_learner(
    body: LearnerCreate,
    session: AsyncSession = Depends(get_session),
):
    """<docstring>"""
    return await create_learner(session, name=body.name, email=body.email)

# Reference:
# items POST -> creates a row in items table, accepts ItemCreate, returns Item with status 201
# learners POST -> creates a row in learners table, accepts LearnerCreate, returns Learner with status 201
