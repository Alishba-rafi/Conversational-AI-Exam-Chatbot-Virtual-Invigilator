from google import genai
from dotenv import load_dotenv
from backend.app.rag.chunker import chunking
import os

load_dotenv()




client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def embedding_chunks():
    chunks = chunking()
    embeddings = []

    for chunk in chunks:
        response = client.models.embed_content(
            model="gemini-embedding-2",
            contents=chunk.page_content
        )

        embeddings.append(response.embeddings[0].values)
    
    return chunks, embeddings

        



    






