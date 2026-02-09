from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate

router = APIRouter(prefix="/projects/{project_id}/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskRead, status_code=201)
async def create_task(project_id: int, payload: TaskCreate, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/", response_model=list[TaskRead])
async def list_tasks(project_id: int, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/{task_id}", response_model=TaskRead)
async def get_task(project_id: int, task_id: int, db: AsyncSession = Depends(get_db)):
    ...


@router.patch("/{task_id}", response_model=TaskRead)
async def update_task(project_id: int, task_id: int, payload: TaskUpdate, db: AsyncSession = Depends(get_db)):
    ...


@router.delete("/{task_id}", status_code=204)
async def delete_task(project_id: int, task_id: int, db: AsyncSession = Depends(get_db)):
    ...
