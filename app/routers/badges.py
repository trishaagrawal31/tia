from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.badge import BadgeCreate, BadgeRead, UserBadgeRead

router = APIRouter(prefix="/badges", tags=["Badges"])


@router.post("/", response_model=BadgeRead, status_code=201)
async def create_badge(payload: BadgeCreate, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/", response_model=list[BadgeRead])
async def list_badges(db: AsyncSession = Depends(get_db)):
    ...


@router.get("/{badge_id}", response_model=BadgeRead)
async def get_badge(badge_id: int, db: AsyncSession = Depends(get_db)):
    ...


# ── User badges ─────────────────────────────────────────

@router.get("/users/{user_id}", response_model=list[UserBadgeRead])
async def list_user_badges(user_id: int, db: AsyncSession = Depends(get_db)):
    ...


@router.post("/users/{user_id}/{badge_id}", response_model=UserBadgeRead, status_code=201)
async def award_badge(user_id: int, badge_id: int, db: AsyncSession = Depends(get_db)):
    ...
