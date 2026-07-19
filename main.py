from backend.app.rag.embedding import embedding_chunks
from backend.app.rag.vector_store import store_chunks
from backend.app.rag.injection import upload_document
from backend.app.rag.generator import generate_answer
from fastapi import FastAPI
from backend.app.API.chat import router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React (Vite)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)


# def main():
   
#     # print("Starting RAG pipeline...")

#     # question = "What is the internship requirement?"

#     # answer = generate_answer(question)

#     # print(answer)


# if __name__ == "__main__":
#     main()