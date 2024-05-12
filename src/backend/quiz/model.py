from typing import Optional
from beanie import Document
from pydantic import BaseModel
import pymongo

from course.model import Course
from tutor.model import Tutor

class QuizQuesion(BaseModel):
    quiz_question: str
    options: list[str]
    correct_answer: str

class Quiz(Document):
    quiz_id: str
    tutor: Tutor
    course: Course
    quiz_questions: Optional[dict[str, QuizQuesion]] = {}
    description: str

    class Settings:
        indexes = [
            pymongo.IndexModel([
                ("quiz_id", pymongo.ASCENDING)
            ], unique=True)
        ]