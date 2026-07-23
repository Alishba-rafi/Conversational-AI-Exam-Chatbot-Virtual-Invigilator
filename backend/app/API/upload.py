from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from backend.app.database.connection import get_db
from backend.app.services.knowledge_base_service import process_upload

router = APIRouter()


@router.post("/upload")
async def upload(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return await process_upload(file, db)