from google import genai
from dotenv import load_dotenv
from backend.app.rag.retriever import retrieve_chunks
from backend.app.services.student_services import build_student_context
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(db, student_id, question):

    # Get student information from SQL database
    student_context = build_student_context(
        db,
        student_id
    )

    # Retrieve relevant RAG chunks
    result = retrieve_chunks(question)

    context = "\n\n".join(
        chunk.chunk_text
        for chunk in result
    )

    # Build prompt
    prompt = f"""
You are a university assistant.

Answer ONLY using the information provided below.

Student Information:
{student_context}

Knowledge Base:
{context}

If the information is unavailable, say:
"I couldn't find that information."

Question:
{question}

Answer:
"""

    # Generate response from Gemini
    response = client.models.generate_content(
       model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text