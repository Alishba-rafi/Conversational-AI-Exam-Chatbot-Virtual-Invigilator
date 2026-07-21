from sqlalchemy.orm import Session

from backend.app.models.StudentResult import StudentResult
from backend.app.models.StudentEnrollment import StudentEnrollment
from backend.app.models.ExamSchedule import ExamSchedule


def get_student_results(db: Session, student_id: int):
    return (
        db.query(StudentResult)
        .filter(StudentResult.student_id == student_id)
        .all()
    )

def get_student_enrollments(db: Session, student_id: int):
    return (
        db.query(StudentEnrollment)
        .filter(StudentEnrollment.student_id == student_id)
        .all()
    )
def get_exam_schedule(db: Session, student_id: int):
    return (
        db.query(ExamSchedule)
        .join(
            StudentEnrollment,
            ExamSchedule.course_code == StudentEnrollment.course_code
        )
        .filter(StudentEnrollment.student_id == student_id)
        .all()
    )

def build_student_context(db: Session, student_id: int):

    results = get_student_results(db, student_id)
    enrollments = get_student_enrollments(db, student_id)
    exams = get_exam_schedule(db, student_id)

    context = "Student Information\n\n"

    context += "Results:\n"

    for result in results:
        context += (
            f"{result.subject_name}: "
            f"{result.marks} "
            f"({result.grade})\n"
        )

    context += "\nEnrolled Courses:\n"

    for course in enrollments:
        context += f"{course.course_name}\n"

    context += "\nExam Schedule:\n"

    for exam in exams:
        context += (
            f"{exam.course_name} - "
            f"{exam.exam_date} "
            f"{exam.exam_time} "
            f"Room {exam.room}\n"
        )

    return context