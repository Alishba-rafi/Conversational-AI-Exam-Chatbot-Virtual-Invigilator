from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector

from backend.app.database.connection import Base


class KnowledgeChunk(Base):
    __tablename__ = "knowledge_chunks"

    id = Column(Integer, primary_key=True, index=True)

    document_name = Column(Text, nullable=False)

    page_number = Column(Integer)

    chunk_index = Column(Integer)

    chunk_text = Column(Text, nullable=False)

    embedding = Column(Vector(3072))

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )