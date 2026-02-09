from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.streak import StreakSnapshotCreate, StreakSnapshotRead, UserStreakStatusRead, StreakEventRead

router = APIRouter(prefix="/users/{user_id}/streaks", tags=["Streaks"])


@router.post("/snapshots", response_model=StreakSnapshotRead, status_code=201)
async def create_streak_snapshot(user_id: int, payload: StreakSnapshotCreate, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/snapshots", response_model=list[StreakSnapshotRead])
async def list_streak_snapshots(user_id: int, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/status", response_model=UserStreakStatusRead)
async def get_streak_status(user_id: int, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/events", response_model=list[StreakEventRead])
async def list_streak_events(user_id: int, db: AsyncSession = Depends(get_db)):
    ...
