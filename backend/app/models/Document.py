
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

from backend.app.database.connection import Base
class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)

    original_name = Column(String(255), nullable=False)
    stored_name = Column(String(255), unique=True, nullable=False)

    file_path = Column(Text, nullable=False)
    file_type = Column(String(20), nullable=False)

    status = Column(String(20), default="PROCESSING")

    uploaded_at = Column(DateTime, default=datetime.utcnow)
    processed_at = Column(DateTime)

    error_message = Column(Text)

    chunks = relationship(
        "KnowledgeChunk",
        back_populates="document",
        cascade="all, delete"
    )