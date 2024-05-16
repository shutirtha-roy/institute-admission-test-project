from typing import Optional
from pydantic import BaseModel
from datetime import date, time

from course.model import Course
from session.model import SessionTypeEnum
from student.model import StudentInfo
from tutor.model import Tutor
from university.model import University


class CreateDTO(BaseModel):
    session_id: str
    host_email: str
    course_code: str
    schedule: str
    description: str
    student_number: int

class UpdateDTO(BaseModel):
    session_id: Optional[str] = None
    description: Optional[str] = None
    student_number: Optional[int] = None


class UpdateStudentListDTO(BaseModel):
    student_email: str

class ResponseDTO(BaseModel):
    session_id: str
    schedule: str
    tutor: Tutor
    course: Course
    university: University
    description: str
    student_number: int
    session_type: SessionTypeEnum
    unapproved_student_list: Optional[list[StudentInfo]]
    approved_student_list: Optional[list[StudentInfo]]