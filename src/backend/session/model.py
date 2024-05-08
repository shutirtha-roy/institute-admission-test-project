from typing import Optional
from beanie import Document
from datetime import date, time

class Tutor(Document):
    session_id: str
    host_name: str
    date: date
    start_time: time
    end_time: time
    student_number: int
    student_list: Optional[list[str]]