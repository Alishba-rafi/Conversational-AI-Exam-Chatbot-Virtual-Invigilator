from datetime import datetime
from sqlalchemy.orm import Session
from backend.app.models.Document import Document

# ------------add record in document table ----------

def create_document(
    db: Session,
    original_name: str,
    stored_name: str,
    file_path: str,
    file_type: str,
):
    document = Document(
        original_name=original_name,
        stored_name=stored_name,
        file_path=file_path,
        file_type=file_type,
        status="PROCESSING"
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document
def update_document_status(
    db: Session,
    document_id: int,
    status: str,
    error_message: str = None
):
    document = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if document is None:
        return

    document.status = status
    document.processed_at = datetime.utcnow()
    document.error_message = error_message

    db.commit()