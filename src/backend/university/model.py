from typing import Optional
from beanie import Document
import pymongo

class University(Document):
    title: str
    description : Optional[str]
    tutor_list: Optional[list[str]]
    course_list: Optional[list[str]]

    class Settings:
        indexes = [
            pymongo.IndexModel([
                ("title", pymongo.ASCENDING)
            ], unique=True)
        ]