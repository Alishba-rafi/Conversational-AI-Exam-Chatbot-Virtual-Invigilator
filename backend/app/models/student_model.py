from sqlalchemy import Column, Integer, String
from backend.app.database.connection import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    roll_number = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    department = Column(String)
    semester = Column(Integer)