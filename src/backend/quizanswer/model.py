from typing import Optional
from beanie import Document
from pydantic import BaseModel
import pymongo

from student.model import StudentInfo

class QuizAnswer(Document):
    quiz_id: str
    student: StudentInfo
    quiz_answers: Optional[str] = ''
    quiz_score: str
    quiz_score_percent: float