from sqlalchemy import Column, Integer, Text,ForeignKey,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector

from backend.app.database.connection import Base


class KnowledgeChunk(Base):
    __tablename__ = "knowledge_chunks"

    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)

    chunk_text = Column(Text, nullable=False)
    embedding = Column(Vector(3072), nullable=False)

    chunk_index = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)

    document = relationship("Document", back_populates="chunks")