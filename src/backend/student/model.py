from typing import Optional
from beanie import Document

class StudentInfo(Document):
    email: str
    name : str
    sessions : Optional[list[str]] = []