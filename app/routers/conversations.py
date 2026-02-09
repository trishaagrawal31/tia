from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.conversation import ConversationCreate, ConversationRead, ConversationUpdate
from app.schemas.message import MessageCreate, MessageRead

router = APIRouter(prefix="/conversations", tags=["Conversations"])


# ── Conversations ───────────────────────────────────────

@router.post("/", response_model=ConversationRead, status_code=201)
async def create_conversation(user_id: int, payload: ConversationCreate, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/", response_model=list[ConversationRead])
async def list_conversations(user_id: int, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/{conversation_id}", response_model=ConversationRead)
async def get_conversation(conversation_id: int, db: AsyncSession = Depends(get_db)):
    ...


@router.patch("/{conversation_id}", response_model=ConversationRead)
async def update_conversation(conversation_id: int, payload: ConversationUpdate, db: AsyncSession = Depends(get_db)):
    ...


@router.delete("/{conversation_id}", status_code=204)
async def delete_conversation(conversation_id: int, db: AsyncSession = Depends(get_db)):
    ...


# ── Messages ────────────────────────────────────────────

@router.post("/{conversation_id}/messages", response_model=MessageRead, status_code=201)
async def create_message(conversation_id: int, payload: MessageCreate, db: AsyncSession = Depends(get_db)):
    ...


@router.get("/{conversation_id}/messages", response_model=list[MessageRead])
async def list_messages(conversation_id: int, db: AsyncSession = Depends(get_db)):
    ...
