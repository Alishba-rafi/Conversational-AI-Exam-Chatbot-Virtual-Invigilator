from fastapi import UploadFile, HTTPException
from backend.app.rag.injection import upload_document
ALLOWED_EXTENSIONS = {".pdf", ".md"}
import os
import pdfplumber
import shutil
from pathlib import Path
from sqlalchemy.orm import Session
from backend.app.services.document_service import create_document,update_document_status


UPLOAD_DIR = Path("backend/app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

#-----------dublicate filename handeling-------

from pathlib import Path

def get_unique_filename(filename: str) -> Path:
    file_path = UPLOAD_DIR / filename

    if not file_path.exists():
        return file_path

    stem = file_path.stem          # exam_rules
    suffix = file_path.suffix      # .pdf

    counter = 1

    while True:
        new_filename = f"{stem} ({counter}){suffix}"
        new_path = UPLOAD_DIR / new_filename

        if not new_path.exists():
            return new_path

        counter += 1

#-----------------validation of file -------------------
def validate_file(file: UploadFile):

    extension = os.path.splitext(file.filename)[1].lower()

    # Check allowed extension
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and Markdown files are allowed."
        )

    # Validate PDF
    if extension == ".pdf":
        try:
            with pdfplumber.open(file.file) as pdf:
                if len(pdf.pages)==0:
                    raise HTTPException(
            status_code=400,
            detail="PDF contains no pages."
        )
                pdf.pages  # Just accessing pages checks if it's a valid PDF
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid PDF file."
            )
            

        # Reset file pointer after reading
        file.file.seek(0)

    # Validate Markdown
    elif extension == ".md":
        try:
            file.file.read().decode("utf-8")
        except UnicodeDecodeError:
            raise HTTPException(
                status_code=400,
                detail="Markdown file must be UTF-8 encoded."
            )

        # Reset file pointer after reading
        file.file.seek(0)
#----------------file save ------------

def save_file(file: UploadFile) -> Path:
    file_path = get_unique_filename(file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path

#------------------Process file-------------
# If you read the stream first, its pointer is at the end, 
# so there's nothing left to copy unless you manually reset it.
# Since your current pipeline works from a saved file, don't call
# await file.read() here. Let save_file() copy the stream directly

async def process_upload(
    file: UploadFile,
    db: Session
):
    # Validate uploaded file
    validate_file(file)

    # Save file to uploads folder
    saved_path = save_file(file)

    extension = os.path.splitext(file.filename)[1].lower()

    # Create document record
    document = create_document(
        db=db,
        original_name=file.filename,
        stored_name=saved_path.name,
        file_path=str(saved_path),
        file_type=extension
    )

    try:
        # Process document (chunking + embedding + vector DB)
        upload_document(
            str(saved_path),
            document.id
        )

        update_document_status(
            db=db,
            document_id=document.id,
            status="READY"
        )

    except Exception as e:

        update_document_status(
            db=db,
            document_id=document.id,
            status="FAILED",
            error_message=str(e)
        )

        raise HTTPException(
            status_code=500,
            detail="Document processing failed."
        )

    return {
        "message": "Document uploaded successfully.",
        "filename": file.filename
    }