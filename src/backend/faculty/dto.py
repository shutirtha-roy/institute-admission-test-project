from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class CreateDTO(BaseModel):
    faculty_name : str
    university_name: str
    description : Optional[str] = ""
    date_created: datetime = datetime.now()


class UpdateDTO(BaseModel):
    faculty_name : Optional[str] = ""
    university_name: Optional[str] = ""
    description : Optional[str] = ""
    date_created: datetime = datetime.now()


class ResponseRoleDTO(BaseModel):
    id: UUID
    faculty_name : str
    university_name: str
    description : str
    date_created: datetime