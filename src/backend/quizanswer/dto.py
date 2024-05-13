from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, root_validator

from course.model import Course
from quiz.model import QuizQuesion
from session.model import Session
from student.model import StudentInfo
from tutor.model import Tutor
from university.model import University


class CreateDTO(BaseModel):
    quiz_id: str
    student_email: str
    quiz_answers: str

class ResponseDTO(BaseModel):
    quiz_id: str
    student: StudentInfo
    quiz_answers: str
    quiz_score: str
    quiz_score_percent: float

class DeleteDTO(BaseModel):
    quiz_id: str
    student_email: str