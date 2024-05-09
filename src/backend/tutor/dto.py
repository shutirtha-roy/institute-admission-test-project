from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, root_validator


class CreateTutorDTO(BaseModel):
    name: Optional[str] = ""
    email: EmailStr
    password: str
    quialifications: Optional[list[str]] = []
    course_list: Optional[list[str]] = []

    @root_validator(pre=True)
    def check_username(cls, values):
        if "email" not in values:
            raise HTTPException(
                status_code=422, detail="Please provide email")
        return values


class UpdateDTO(BaseModel):
    tutor_name : Optional[str] = None
    quialifications: Optional[list[str]] = None


class addCourseDTO(BaseModel):
    course_code: str

class ResponseRoleDTO(BaseModel):
    tutor_name : str
    tutor_email: EmailStr
    quialifications: Optional[list[str]]
    course_list: Optional[list[str]]