from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.research_project import (
    ProjectCreate, ProjectRead, ProjectUpdate,
    ProjectFacultyCreate, ProjectFacultyRead,
)

router = APIRouter(prefix="/projects", tags=["Research Projects"])


# ── Projects ────────────────────────────────────────────

@router.post("/", response_model=ProjectRead, status_code=201)
async def create_project(owner_user_id: int, payload: ProjectCreate, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/", response_model=list[ProjectRead])
async def list_projects(owner_user_id: int | None = None, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/{project_id}", response_model=ProjectRead)
async def get_project(project_id: int, db: AsyncSession = Depends(get_db)):
    ...


@router.patch("/{project_id}", response_model=ProjectRead)
async def update_project(project_id: int, payload: ProjectUpdate, db: AsyncSession = Depends(get_db)):
    ...


@router.delete("/{project_id}", status_code=204)
async def delete_project(project_id: int, db: AsyncSession = Depends(get_db)):
    ...


# ── Project Faculty ─────────────────────────────────────

@router.post("/{project_id}/faculty", response_model=ProjectFacultyRead, status_code=201)
async def add_faculty_to_project(project_id: int, payload: ProjectFacultyCreate, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/{project_id}/faculty", response_model=list[ProjectFacultyRead])
async def list_project_faculty(project_id: int, db: AsyncSession = Depends(get_db)):
    ...


@router.delete("/{project_id}/faculty/{project_faculty_id}", status_code=204)
async def remove_faculty_from_project(project_id: int, project_faculty_id: int, db: AsyncSession = Depends(get_db)):
    ...
