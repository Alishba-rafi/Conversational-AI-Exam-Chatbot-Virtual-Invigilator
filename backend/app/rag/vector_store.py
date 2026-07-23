from backend.app.database.connection import SessionLocal
from backend.app.models.Knowledge_chunk import KnowledgeChunk


def store_chunks(chunks, embeddings, document_id):
    """
    Store chunk text and their embeddings into PostgreSQL.
    """

    db =SessionLocal() # get connection with database open connection 
    try:
        for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):  # zip create pair 
# create one row of table 
            record = KnowledgeChunk(
                document_id=document_id,
               
                chunk_index=index,
                chunk_text=chunk.page_content,
                embedding=embedding
            )

            db.add(record)

        db.commit()

        print(f" Stored {len(chunks)} chunks successfully.")

    except Exception as e:
        db.rollback()
        print(" Error while storing chunks:", e)
        raise

    finally:
        db.close()