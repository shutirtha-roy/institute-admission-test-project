from enum import Enum
from typing import Optional
from beanie import Document
from datetime import date, time

import pymongo

from course.model import Course
from student.model import StudentInfo
from tutor.model import Tutor
from university.model import University

class SessionTypeEnum(str, Enum):
    PRIVATE = "private"
    GROUP = "group"

class Session(Document):
    session_id: str
    tutor: Tutor
    course: Course
    university: University
    schedule: str
    description: str
    student_number: int
    session_type: SessionTypeEnum
    unapproved_student_list: Optional[list[StudentInfo]] = []
    approved_student_list: Optional[list[StudentInfo]] = []

    class Settings:
        indexes = [
            pymongo.IndexModel([
                ("session_id", pymongo.ASCENDING)
            ], unique=True)
        ]