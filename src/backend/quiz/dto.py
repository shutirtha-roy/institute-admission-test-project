from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, root_validator

from course.model import Course
from quiz.model import QuizQuesion
from session.model import Session
from university.model import University


class CreateDTO(BaseModel):
    quiz_id: str
    quiz_code: str

class AddQuestionDto(BaseModel):
    question_number: str
    quiz_question: str
    options: str
    correct_answer: str

class DeleteQuestionDto(BaseModel):
    question_number: str

class ResponseDTO(BaseModel):
    quiz_id: str
    quiz_code: str
    quiz_questions: Optional[dict[str, QuizQuesion]]