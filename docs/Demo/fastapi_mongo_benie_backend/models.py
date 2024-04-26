from beanie import Document
from datetime import datetime

class Students(Document):
    student_name : str
    gender : str
    date_created: datetime = datetime.now()

    class Config:
        schema = {
            "student_name" : "Tirtha Toy",
            "gender": "Non-binary",
        }