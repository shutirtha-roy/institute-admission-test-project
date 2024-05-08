from typing import Optional
from pydantic import BaseModel


class CreateDTO(BaseModel):
    tutor_email: str
    tutor_name : str
    quialifications: Optional[list[str]]
    course_list: Optional[list[str]]


class UpdateDTO(BaseModel):
    tutor_name : Optional[str]
    quialifications: Optional[list[str]]
    course_list: Optional[list[str]]


class ResponseRoleDTO(BaseModel):
    tutor_email: str
    tutor_name : str
    quialifications: Optional[list[str]]
    course_list: Optional[list[str]]