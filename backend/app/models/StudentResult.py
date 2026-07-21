from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app.database.connection import Base

class StudentResult(Base):
    __tablename__ = "student_results"

    result_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    subject_name = Column(String(100), nullable=False)
    marks = Column(Integer, nullable=False)
    grade = Column(String(5))
    semester = Column(Integer)