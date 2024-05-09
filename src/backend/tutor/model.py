from typing import Optional
from beanie import Document

class Tutor(Document):
    tutor_email: str
    tutor_name : str
    qualification_list: Optional[list[str]]
    course_list: Optional[list[str]]