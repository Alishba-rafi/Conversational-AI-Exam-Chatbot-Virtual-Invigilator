from google import genai
from dotenv import load_dotenv
from backend.app.rag.retriever import retrieve_chunks
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_answer(question):

    result = retrieve_chunks(question)

    context = "\n\n".join(
        chunk.chunk_text
        for chunk in result
    )

    prompt = f"""
You are a helpful university assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context, say:
"I couldn't find that information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

    return response.text