from datetime import datetime
from uuid import UUID
from fastapi import APIRouter
from beanie.operators import In

from course.model import Course
from error.exception import EntityNotFoundError, UnauthorizedError
from tutor.model import Tutor
from university.dto import CreateDTO, UpdateDTO, ResponseDTO
from university.model import University
from utils import utils

university_router = APIRouter(tags=["University"])

@university_router.post("/", status_code = 201)  
async def createuniversity(data: CreateDTO):
    try:
        university = University(**data.model_dump())

        await university.save()

        return utils.create_response(
            status_code=201,
            success=True,
            message="University has been created successfully",
            data=ResponseDTO(**university.model_dump())
        )
    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e))
    

@university_router.get('/getalluniversity', status_code=200)
async def getalluniversity():
    try:
        universities = await University.find_all().to_list()

        return utils.create_response(
            status_code=200,
            success=True,
            message="University List has been retrieved successfully",
            result=[ResponseDTO(**r.model_dump()) for r in universities],
        )

    except UnauthorizedError as ue:
        return utils.create_response(
            status_code=ue.status_code,
            success=False,
            message=ue.message
        )
    except Exception as e:
        return utils.create_response(
            status_code=500,
            success=False,
            message=str(e)
        )
    

@university_router.get('/getuniversity/{university_title}', status_code=200)
async def getoneuniversity(university_title:str):
    try:
        university = await University.find_one(
            University.title == university_title
        )

        if university is None:
            raise EntityNotFoundError

        return utils.create_response(
            status_code=200,
            success=True,
            message="University List has been retrieved successfully",
            result= ResponseDTO(**university.model_dump()),
        )

    except UnauthorizedError as ue:
        return utils.create_response(
            status_code=ue.status_code,
            success=False,
            message=ue.message
        )
    except Exception as e:
        return utils.create_response(
            status_code=500,
            success=False,
            message=str(e)
        )

@university_router.patch('/updateuniversity/{university_title}', status_code=200)
async def updateuniversity(university_title:str, data: UpdateDTO):
    try:
        university = await University.find_one(
            University.title == university_title
        )

        if university is None:
            raise EntityNotFoundError
        
        if(data.title):
            university.title = data.title

        if(data.description):
            university.description = data.description

        if(data.course_list):
            university.course_list = data.course_list

        if(data.tutor_list):
            university.tutor_list = data.tutor_list

        university.save()

        return utils.create_response(
            status_code=200,
            success=True,
            message="University List has been retrieved successfully",
            result= ResponseDTO(**university.model_dump()),
        )

    except UnauthorizedError as ue:
        return utils.create_response(
            status_code=ue.status_code,
            success=False,
            message=ue.message
        )
    except Exception as e:
        return utils.create_response(
            status_code=500,
            success=False,
            message=str(e)
        )
    

@university_router.delete("/{university_title}", status_code = 200)
async def delete(university_title:str):
    try: 
        university = await University.find_one(
            University.title == university_title
        )
        
        if university is None:
            raise EntityNotFoundError

        courses = await Course.find(
            Course.university_title == university_title
        ).to_list()

        if courses is None:
            raise EntityNotFoundError
        
        tutors = []
        for course in courses:
            tutor_names = course.tutor_list
            for x in tutor_names:
                tutor = await Tutor.find_one(Tutor.tutor_name == x)
                
                tutor.course_list.remove(course.course_code)

                await tutor.save()

            await course.delete()

        await university.delete()

        return utils.create_response(
            status_code=200,
            success=True,
            message="University has been deleted successfully",
        )
   
    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 