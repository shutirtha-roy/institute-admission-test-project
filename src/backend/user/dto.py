from datetime import datetime
from typing import Annotated, Optional
from uuid import UUID
from fastapi import HTTPException
from pydantic import AfterValidator, BaseModel, EmailStr, root_validator
import re

from user.model import UserTypeEnum


def password_validator(password: str) -> str:
    # pattern = r"^(?=.*[A-Za-z])(?=.*\d)[@$!%*#?&A-Za-z\d]{8,}$"
    # if not re.match(pattern, password):
    #     raise HTTPException(
    #         status_code=422,
    #         detail="Password must contain at least one letter, one number and one special character",
    #     )
    return password

class CreateUserDTO(BaseModel):
    name: Optional[str] 
    email: EmailStr
    password: Annotated[str, AfterValidator(password_validator)]

    @root_validator(pre=True)
    def check_username(cls, values):
        if "email" not in values:
            raise HTTPException(
                status_code=422, detail="Please provide email or phone number")
        return values

class LoginUserDTO(BaseModel):
    email: EmailStr
    password: str

    @root_validator(pre=True)
    def check_dto(cls, values):
        if "email" not in values:
            raise HTTPException(
                status_code=422, detail="Please provide email")

        if ("email" in values) and "password" not in values:
            raise HTTPException(
                status_code=422, detail="Please provide password")
        return values


class UpdateDTO(BaseModel):
    name: Optional[str] = None
    permissions: Optional[dict[str, int]] = None


class ResponseUserDTO(BaseModel):
    name: str
    email: str
    role: UserTypeEnum