from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.app.schemas.chat import ChatRequest, ChatResponse
from backend.app.rag.generator import generate_answer
from backend.app.database.connection import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    try:
        answer = generate_answer(
            db,
            request.student_id,
            request.question
        )

        return ChatResponse(answer=answer)

    except Exception as e:
        raise HTTPException(
            status_code=500,
 detail=str(e) 
        )