from backend.app.rag.embedding import embedding_chunks
from backend.app.rag.vector_store import store_chunks


def main():

    print("Starting RAG pipeline...")

    document_name = "sample.pdf"

    chunks, embeddings = embedding_chunks()

    print(f"Chunks Generated: {len(chunks)}")
    print(f"Embeddings Generated: {len(embeddings)}")

    store_chunks(
        chunks=chunks,
        embeddings=embeddings,
        document_name=document_name
    )

    print("Data stored successfully.")


if __name__ == "__main__":
    main()