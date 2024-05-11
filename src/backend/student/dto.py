from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, root_validator

from course.model import Course
from session.model import Session
from university.model import University



class UpdateDTO(BaseModel):
    email: str
    name : str

class ResponseDTO(BaseModel):
    email: str
    name : str
    sessions : Optional[list[Session]] = []
    courses : Optional[list[Course]] = []
    university : Optional[list[University]] = []