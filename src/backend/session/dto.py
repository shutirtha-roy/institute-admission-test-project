from typing import Optional
from pydantic import BaseModel
from datetime import date, time


class CreateDTO(BaseModel):
    session_id: str
    host_name: str
    date: date
    start_time: time
    end_time: time
    student_number: int
    student_list: Optional[list[str]]

class UpdateDTO(BaseModel):
    session_id: Optional[str]
    host_name: Optional[str]
    date: Optional[date]
    start_time: Optional[time]
    end_time: Optional[time]
    student_number: Optional[int]
    student_list: Optional[list[str]]


class ResponseRoleDTO(BaseModel):
    tutor_email: str
    tutor_name : str
    quialifications: Optional[list[str]]
    course_list: Optional[list[str]]