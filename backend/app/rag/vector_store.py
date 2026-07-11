from database.connection import SessionLocal
from database.model import KnowledgeChunk


def store_chunks(chunks, embeddings, document_name):
    """
    Store chunk text and their embeddings into PostgreSQL.
    """

    db = SessionLocal()

    try:
        for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

            record = KnowledgeChunk(
                document_name=document_name,
                page_number=chunk.metadata.get("page", 0),
                chunk_index=index,
                chunk_text=chunk.page_content,
                embedding=embedding
            )

            db.add(record)

        db.commit()

        print(f"✅ Stored {len(chunks)} chunks successfully.")

    except Exception as e:
        db.rollback()
        print("❌ Error while storing chunks:", e)
        raise

    finally:
        db.close()