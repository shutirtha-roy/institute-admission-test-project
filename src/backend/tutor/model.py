from typing import Optional
from beanie import Document

class Tutor(Document):
    tutor_email: str
    tutor_name : str
    quialifications: Optional[list[str]]
    course_list: Optional[list[str]]