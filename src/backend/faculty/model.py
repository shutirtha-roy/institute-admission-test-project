from typing import Optional
from beanie import Document
from datetime import datetime

class Faculty(Document):
    faculty_name : str
    university_name: str
    description : Optional[str]
    date_created: datetime = datetime.now()