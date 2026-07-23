from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.API.chat import router as chat_router
from backend.app.API.auth import router as auth_router
from backend.app.API.upload import router as upload_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(auth_router)
app.include_router(upload_router)

# def main():
   
#     # print("Starting RAG pipeline...")

#     # question = "What is the internship requirement?"

#     # answer = generate_answer(question)

#     # print(answer)


# if __name__ == "__main__":
#     main()
