from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from backend.app.schemas.chat import ChatRequest
from backend.app.rag.generator import generate_answer
from backend.app.database.connection import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#now we are not returning json 
@router.post("/chat")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    try:

        return StreamingResponse(
            generate_answer(
                db,
                request.student_id,
                request.question
            ),
            media_type="text/event-stream"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )