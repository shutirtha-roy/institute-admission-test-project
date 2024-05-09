from typing import Optional
from pydantic import BaseModel


class CreateDTO(BaseModel):
    title: str
    description : Optional[str] = ''
    tutor_list: Optional[list[str]] = []
    course_list: Optional[list[str]] = []


class UpdateDTO(BaseModel):
    title: Optional[str] = None
    description : Optional[str] = None
    tutor_list: Optional[list[str]] = None
    course_list: Optional[list[str]] = None


class ResponseDTO(BaseModel):
    title: str
    description : Optional[str] = ''
    tutor_list: Optional[list[str]] = []
    course_list: Optional[list[str]] = []