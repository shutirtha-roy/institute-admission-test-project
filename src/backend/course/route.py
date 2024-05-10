import asyncio
from datetime import datetime
from uuid import UUID
from fastapi import APIRouter

from error.exception import EntityNotFoundError, UnauthorizedError
from course.dto import CreateDTO, UpdateDTO, ResponseDTO
from course.model import Course
from university.model import University
from utils import utils

course_router = APIRouter(tags=["Course"])

@course_router.post("/coursecreate", status_code = 201)  
async def createcourse(data: CreateDTO):
    try:
        university = await University.find_one(University.title == data.university_title)

        if university is None:
            raise EntityNotFoundError("University Not Found")
        
        course = Course(**data.model_dump())

        university.course_list.append(course.title)

        await course.save()
        await university.save() 

        return utils.create_response(
            status_code=201,
            success=True,
            message="Course has been created successfully",
            data=ResponseDTO(**course.model_dump())
        )
    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    
    except EntityNotFoundError as en:
        return utils.create_response(status_code=en.status_code, success=False, message=en.message)
    
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e))
    

@course_router.get('/getallcourses', status_code=200)
async def getalluniversity():
    try:
        courses = await Course.find_all().to_list()

        return utils.create_response(
            status_code=200,
            success=True,
            message="Course List has been retrieved successfully",
            result=[ResponseDTO(**r.model_dump()) for r in courses],
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
    

@course_router.get('/getcoursebycode/{course_code}', status_code=200)
async def getcoursebycode(course_code:str):
    try:
        course = await Course.find_one(
            Course.course_code == course_code
        )

        if course is None:
            raise EntityNotFoundError

        return utils.create_response(
            status_code=200,
            success=True,
            message="Course has been retrieved successfully",
            result= ResponseDTO(**course.model_dump()),
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
    

@course_router.get('/getcoursebyuniversity/{university_title}', status_code=200)
async def getcoursebyuniversity(university_title:str):
    try:
        courses = await Course.find(
            Course.university_title == university_title
        ).to_list()

        if courses is None:
            raise EntityNotFoundError

        return utils.create_response(
            status_code=200,
            success=True,
            message="Course List has been retrieved successfully",
            result= [ResponseDTO(**r.model_dump()) for r in courses],
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
    

@course_router.patch('/updatecourse/{course_code}', status_code=200)
async def updatecourse(course_code:str, data: UpdateDTO):
    try:
        course = await Course.find_one(
            Course.course_code == course_code
        )

        if course is None:
            raise EntityNotFoundError
        
        if(data.title):
            course.title = data.title

        if(data.course_code):
            course.course_code = data.course_code

        if(data.university_title):
            course.university_title = data.university_title

        if(data.description):
            course.description = data.description

        if(data.tutor_list):
            course.tutor_list = data.tutor_list

        course.save()

        return utils.create_response(
            status_code=200,
            success=True,
            message="University List has been retrieved successfully",
            result= ResponseDTO(**course.model_dump()),
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
    

@course_router.delete("/{course_code}", status_code = 200)
async def delete(course_code:str):
    try: 
        course = await Course.find_one(
            Course.course_code == course_code
        )

        if course is None:
            raise EntityNotFoundError
        
        university = await University.find_one(University.title == course.university_title)

        if university is None:
            raise EntityNotFoundError

        university.course_list.remove(course.title)
        
        await course.delete()
        await university.save()

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