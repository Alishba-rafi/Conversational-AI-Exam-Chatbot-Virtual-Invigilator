from pydantic import BaseModel, Field, field_validator 
# pydantic is for structure data

class ChatRequest(BaseModel):
    student_id: int
    question: str = Field(
        min_length=1,
        max_length=500
    )


    @field_validator("question") #@  tell "Before accepting the question field, call the function below.
    @classmethod
    def validate_question(cls, value):
        if not value.strip(): # remove space 
            raise ValueError("Question cannot be empty.")
        return value


class ChatResponse(BaseModel):
    answer: str