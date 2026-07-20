from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    question: str = Field(
        min_length=1,
        max_length=500,
        description="Student's question"
    )

class ChatResponse(BaseModel):
    answer: str