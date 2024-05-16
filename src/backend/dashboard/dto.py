from pydantic import BaseModel


class StudentEmailDto(BaseModel):
    student_email: str