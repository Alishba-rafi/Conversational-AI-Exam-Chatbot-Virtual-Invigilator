from pydantic import BaseModel

class LoginRequest(BaseModel):
    roll_number: str
    password: str


class LoginResponse(BaseModel):
    student_id: int
    full_name: str
    message: str