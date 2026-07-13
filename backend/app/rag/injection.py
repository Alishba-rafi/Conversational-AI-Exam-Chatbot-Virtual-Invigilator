from  backend.app.rag.embedding  import embedding_chunks
from backend.app.rag.vector_store import store_chunks
import os

def upload_document(document_path):
    chunks, embeddings = embedding_chunks(document_path)

    print(f"Chunks Generated: {len(chunks)}")
    print(f"Embeddings Generated: {len(embeddings)}")

    document_name = os.path.basename(document_path)

    store_chunks(
        chunks=chunks,
        embeddings=embeddings,
        document_name=document_name
    )

    print("Data stored successfully.")