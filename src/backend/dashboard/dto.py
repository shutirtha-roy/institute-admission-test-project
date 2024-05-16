from pydantic import BaseModel


class StudentEmailDto(BaseModel):
    student_email: str

class AdminDashboardDto(BaseModel):
    number_of_students: int
    number_of_tutors: int
    my_base64_jpgData: str