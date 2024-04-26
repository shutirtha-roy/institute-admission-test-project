from fastapi import APIRouter

from dto import CreateDTO
from models import Students

student_router = APIRouter()

@student_router.get('/', status_code=200)
async def getallstudents():
    students = await Students.find_all().to_list()
    
    return students

@student_router.get('/{task_id}')
async def getonestudent(task_id):
    pass

@student_router.post("/studentcreate", status_code=201)
async def createstudent(data: CreateDTO):
    student = Students(
        student_name= data.student_name,
        gender= data.gender,
        date_created= data.date_created
    )

    await student.save()
    
    return {"massege" : "Student Created successfully"}

@student_router.patch('/')
async def changestudentinfo():
    pass

@student_router.delete('/')
async def deletestudent():
    pass