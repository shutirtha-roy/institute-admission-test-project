from typing import Optional
from beanie import Document
from pydantic import BaseModel

class QuizQuesion(BaseModel):
    # question_number: str
    quiz_question: str
    options: list[str]
    correct_answer: str

class Quiz(Document):
    quiz_id: str
    quiz_code: str
    quiz_questions: Optional[dict[str, QuizQuesion]] = {}