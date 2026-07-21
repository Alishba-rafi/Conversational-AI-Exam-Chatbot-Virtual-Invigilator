from sqlalchemy import Column, Integer, String, ForeignKey
from backend.app.database.connection import Base

class StudentEnrollment(Base):
    __tablename__ = "student_enrollments"

    enrollment_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_code = Column(String(20))
    course_name = Column(String(100))
    semester = Column(Integer)