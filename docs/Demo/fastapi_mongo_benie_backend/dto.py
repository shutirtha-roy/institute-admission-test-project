from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class CreateDTO(BaseModel):
    student_name : str
    gender : str
    date_created: Optional[datetime] = datetime.now()


class UpdateDTO(BaseModel):
    name: Optional[str] = None
    permissions: Optional[dict[str, int]] = None


class ResponseRoleDTO(BaseModel):
    id: UUID
    student_name : str
    gender : str
    date_created: datetime