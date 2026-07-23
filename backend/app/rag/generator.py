from google import genai
from dotenv import load_dotenv
from backend.app.rag.retriever import retrieve_chunks
from backend.app.services.student_services import build_student_context
import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_answer(db, student_id, question):

    # Get student information
    student_context = build_student_context(db, student_id)

    # Retrieve RAG chunks
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

    # Stream response from Gemini
    stream = client.models.generate_content_stream(
        model="gemini-3.5-flash",
        contents=prompt
    )

    try:
        for chunk in stream:
            if (
                chunk.candidates
                # Why "candidates"?
                # Because Gemini may generate multiple possible answers.
                # Usually it gives only one.
                and chunk.candidates[0].content
                and chunk.candidates[0].content.parts
            ):
                for part in chunk.candidates[0].content.parts:
                    # hasattr(object, "attribute")
                    # Does this object have this property?"
                    if hasattr(part, "text") and part.text:
                        # array of each word
                        words = part.text.split()

                        for word in words:
                            # send word by word
                            yield word + " "
                            time.sleep(0.1)

    except Exception as e:
        print("STREAM ERROR:", repr(e))
        raise