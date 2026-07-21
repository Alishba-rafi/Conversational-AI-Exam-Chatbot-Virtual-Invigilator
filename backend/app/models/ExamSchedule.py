from sqlalchemy import Column, Integer, String, Date, Time
from backend.app.database.connection import Base

class ExamSchedule(Base):
    __tablename__ = "exam_schedule"

    exam_id = Column(Integer, primary_key=True, index=True)
    course_code = Column(String(20))
    course_name = Column(String(100))
    exam_date = Column(Date)
    exam_time = Column(Time)
    room = Column(String(20))
    semester = Column(Integer)