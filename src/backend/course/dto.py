from typing import Optional
from pydantic import BaseModel


class CreateDTO(BaseModel):
    title: str
    course_code: str
    university_title: str
    description : Optional[str] = None
    tutor_list: Optional[list[str]] = []
    
class UpdateDTO(BaseModel):
    title: Optional[str] = None
    course_code: Optional[str] = None
    university_title: Optional[str] = None
    description : Optional[str] = None
    tutor_list: Optional[list[str]] = None

class ResponseDTO(BaseModel):
    title: str
    course_code: str
    university_title: str
    description : Optional[str] = None
    tutor_list: Optional[list[str]] = []