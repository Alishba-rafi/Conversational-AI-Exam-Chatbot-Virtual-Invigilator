from database.connection import SessionLocal
from database.model import KnowledgeChunk


def store_chunks(chunks, embeddings, document_name):

    db = SessionLocal()

    try:

        for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

            row = KnowledgeChunk(
                document_name=document_name,
                page_number=chunk.metadata.get("page", 0),
                chunk_index=index,
                chunk_text=chunk.page_content,
                embedding=embedding
            )

            db.add(row)

        db.commit()

    finally:
        db.close()