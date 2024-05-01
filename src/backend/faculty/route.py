from fastapi import APIRouter

from faculty.dto import CreateDTO, ResponseRoleDTO
from faculty.model import Faculty

faculty_router = APIRouter(tags=["Faculty"])

@faculty_router.get('/', status_code=200)
async def getallfaculty():
    faculties = await Faculty.find_all().to_list()
    
    return faculties

@faculty_router.get('/{faculty_id}')
async def getonestudent(faculty_id):
    pass

@faculty_router.post("/facultycreate", status_code=201)
async def createfaculty(data: CreateDTO):
    faculty = Faculty(
        faculty_name= data.faculty_name,
        university_name= data.university_name,
        description= data.description,
        date_created= data.date_created
    )

    await faculty.save()
    
    return {"massege" : "Faculty Created successfully"}

@faculty_router.patch('/')
async def changestudentinfo():
    pass

@faculty_router.delete('/')
async def deletestudent():
    pass