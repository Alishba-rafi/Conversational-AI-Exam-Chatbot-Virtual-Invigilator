from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Hello, who are you?"
    )

    print(response.text)

except Exception as e:
    print("Error:", e)


# from backend.app.database.connection import SessionLocal
# from backend.app.models.student_model import Student

# db = SessionLocal()

# student = db.query(Student).first()

# print(student.full_name)