from backend.app.rag.embedding import embedding_chunks
from backend.app.rag.vector_store import store_chunks
from backend.app.rag.injection import upload_document
from backend.app.rag.generator import generate_answer


def main():
    print("Starting RAG pipeline...")

    question = "What is the internship requirement?"

    answer = generate_answer(question)

    print(answer)


if __name__ == "__main__":
    main()