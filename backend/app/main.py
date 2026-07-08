from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to the Conversational AI Exam Chatbot API!"
    }

@app.get("/health")
def health():
    return {
        "status": "running"
    }