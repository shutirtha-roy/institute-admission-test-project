from pydantic import BaseModel

from course.model import Course
from quiz.model import Quiz
from student.model import StudentInfo


class CreateDTO(BaseModel):
    quiz_id: str
    student_email: str
    quiz_answers: str

class ResponseDTO(BaseModel):
    quiz_id: str
    student: StudentInfo
    course: Course
    quiz_answers: str
    quiz_score: str
    quiz_score_percent: float

class DeleteDTO(BaseModel):
    quiz_id: str
    student_email: str

class CourseResponseDTO(BaseModel):
    course: Course
    quizes: list[ResponseDTO]

class StudentEmailDto(BaseModel):
    student_email: str

class StudentGivenQuizDto(BaseModel):
    course_quizes: list[Quiz]
    given_quizes: list[Quiz]