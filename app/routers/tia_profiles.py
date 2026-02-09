from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.tia_profile import TiaProfileCreate, TiaProfileRead, TiaProfileUpdate

router = APIRouter(prefix="/users/{user_id}/tia-profiles", tags=["TIA Profiles"])


@router.post("/", response_model=TiaProfileRead, status_code=201)
async def create_tia_profile(user_id: int, payload: TiaProfileCreate, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/", response_model=list[TiaProfileRead])
async def list_tia_profiles(user_id: int, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/{profile_id}", response_model=TiaProfileRead)
async def get_tia_profile(user_id: int, profile_id: int, db: AsyncSession = Depends(get_db)):
    ...


@router.patch("/{profile_id}", response_model=TiaProfileRead)
async def update_tia_profile(user_id: int, profile_id: int, payload: TiaProfileUpdate, db: AsyncSession = Depends(get_db)):
    ...


@router.delete("/{profile_id}", status_code=204)
async def delete_tia_profile(user_id: int, profile_id: int, db: AsyncSession = Depends(get_db)):
    ...
