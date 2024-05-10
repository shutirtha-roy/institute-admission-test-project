from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, root_validator

from course.model import Course



class UpdateDTO(BaseModel):
    email: str
    name : str

class ResponseDTO(BaseModel):
    email: str
    name : str
    courses: Optional[list[Course]] = []
    sessions : Optional[list[str]] = []