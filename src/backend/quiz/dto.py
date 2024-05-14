from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, root_validator

from course.model import Course
from quiz.model import QuizQuesion
from session.model import Session
from tutor.model import Tutor
from university.model import University


class CreateDTO(BaseModel):
    quiz_id: str
    tutor_email: str
    course_code: str
    description: str


class AddQuestionDto(BaseModel):
    question_number: str
    quiz_question: str
    options: str
    correct_answer: str

class DeleteQuestionDto(BaseModel):
    question_number: str

class ResponseDTO(BaseModel):
    quiz_id: str
    tutor: Tutor
    course: Course
    description: str
    quiz_questions: Optional[dict[str, QuizQuesion]]

class QuizQuestionResponseDTO(BaseModel):
    question_number: str
    quiz_question: str
    options: list[str]
    correct_answer: str