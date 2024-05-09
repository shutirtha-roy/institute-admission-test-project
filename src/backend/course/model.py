from typing import Optional
from beanie import Document
import pymongo

class Course(Document):
    title: str
    course_code: str
    university_title: str
    description : Optional[str]
    tutor_list: Optional[list[str]]

    class Settings:
        indexes = [
            pymongo.IndexModel([
                ("title", pymongo.ASCENDING), ("course_code", pymongo.ASCENDING)
            ], unique=True)
        ]