from google import genai
from dotenv import load_dotenv
from backend.app.rag.chunker import chunking
import os

load_dotenv()

# print("Current Directory:", os.getcwd())
# print("API Key:", os.getenv("GEMINI_API_KEY"))


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def embedding_chunks(Document_Path):
    chunks = chunking(Document_Path)
    embeddings = []

    for chunk in chunks:
        response = client.models.embed_content(
            model="gemini-embedding-2",
            contents=chunk.page_content
        )

        embeddings.append(response.embeddings[0].values)
    
    return chunks, embeddings

        
def get_embedding(text):
    response = client.models.embed_content(
        model="gemini-embedding-2",
        contents=text
    )

    return response.embeddings[0].values


    






