from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.connection import SessionLocal
from backend.app.models.student_model import Student
from backend.app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login", response_model=LoginResponse)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    # Find student by roll number and password
    student = (
        db.query(Student)
        .filter(
            Student.roll_number == request.roll_number,
            Student.password == request.password
        )
        .first()
    )

    # If no student is found
    if not student:
        raise HTTPException(
            status_code=401,
            detail="Invalid roll number or password"
        )

    # Login successful
    return LoginResponse(
        student_id=student.student_id,
        full_name=student.full_name,
        message="Login successful"
    )