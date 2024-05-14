from typing import Optional
from beanie import Document
from pydantic import BaseModel
import pymongo

from course.model import Course
from student.model import StudentInfo

class QuizAnswer(Document):
    quiz_id: str
    student: StudentInfo
    course: Course
    quiz_answers: Optional[str] = ''
    quiz_score: str
    quiz_score_percent: float
