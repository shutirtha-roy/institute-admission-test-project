from typing import Optional
from beanie import Document

from course.model import Course

class StudentInfo(Document):
    email: str
    name : str
    courses: Optional[list[Course]] = []
    sessions : Optional[list[str]] = []