import asyncio
import bcrypt
from fastapi import APIRouter

from course.model import Course
from error.exception import EntityNotFoundError, UnauthorizedError
from tutor.dto import CreateTutorDTO, ResponseRoleDTO, UpdateDTO, addCourseDTO
from tutor.model import Tutor
from university.model import University
from user.model import User, UserTypeEnum
from utils import utils

tutor_router = APIRouter(tags=["Tutor"])


@tutor_router.post("/tutorcreate", status_code=201)
async def createtutor(data: CreateTutorDTO):
    try:
        tutor = User(
            name= data.name,
            email= data.email,
            password= bcrypt.hashpw(
                data.password.encode("utf-8"), bcrypt.gensalt()),
            role= UserTypeEnum.TUTOR,
            approved= True
        )
        tutor_info = Tutor(
            tutor_email = data.email,
            tutor_name = data.name,
            qualifications= data.qualifications,
            course_list=[]
        )
        print(3)
        await tutor.save() 
        await tutor_info.save()
        
        return utils.create_response(
                status_code=201,
                success=True,
                message="Tutor Created successfully",
                data=ResponseRoleDTO(**tutor_info.model_dump())
            )
    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    
    except EntityNotFoundError as en:
        return utils.create_response(status_code=en.status_code, success=False, message=en.message)
    
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e))
    

@tutor_router.get('/alltutor', status_code=200)
async def getalltutors():
    try:
        tutors = await Tutor.find_all().to_list()

        return utils.create_response(
            status_code=200,
            success=True,
            message="Tutor List has been retrieved successfully",
            result=[ResponseRoleDTO(**r.model_dump()) for r in tutors],
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


@tutor_router.patch("/changetutorinfo/{tutorEmail}")
async def changetutorinfo(tutorEmail:str, data: UpdateDTO):
    try:
        tutor = await User.find_one(
                User.email == tutorEmail,
                User.role == UserTypeEnum.TUTOR,
            )
        if tutor is None:
            raise EntityNotFoundError
        
        tutor_info = await Tutor.find_one(
            Tutor.tutor_email == tutorEmail,
        )

        if tutor_info is None:
            raise EntityNotFoundError
        
        if data.tutor_name:
            tutor.name = data.tutor_name
            tutor_info.tutor_name = data.tutor_name 

        if data.qualifications:
            tutor_info.qualifications = data.qualifications

        await tutor.save()
        await tutor_info.save()

        return utils.create_response(
                status_code=200,
                success=True,
                message="Tutor updated successfully.",
                data = ResponseRoleDTO(**tutor_info.model_dump())
            )
    
    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@tutor_router.patch("/addtutorcourse/{tutorEmail}")
async def addtutorcourse(tutorEmail:str, data: addCourseDTO):
    try:
        tutor_info = await Tutor.find_one(
            Tutor.tutor_email == tutorEmail
        )

        if tutor_info is None:
            raise EntityNotFoundError
        
        course = await Course.find_one(
            Course.course_code == data.course_code
        ) 

        if course is None:
            raise EntityNotFoundError
        
        university = await University.find_one(University.title == course.university_title)

        if university is None:
            raise EntityNotFoundError
        
        tutor_info.course_list.append(course.course_code)
        course.tutor_list.append(tutor_info.tutor_name)

        if (tutor_info.tutor_name not in university.tutor_list):
            university.tutor_list.append(tutor_info.tutor_name)

        await tutor_info.save()
        await course.save()
        await university.save()

        return utils.create_response(
                status_code=200,
                success=True,
                message="Course added to tutor successfully.",
                data = ResponseRoleDTO(**tutor_info.model_dump())
            )
    
    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@tutor_router.patch("/removetutorcourse/{tutorEmail}")
async def addtutorcourse(tutorEmail:str, data: addCourseDTO):
    try:
        tutor_info = await Tutor.find_one(
            Tutor.tutor_email == tutorEmail
        )

        if tutor_info is None:
            raise EntityNotFoundError
        
        course = await Course.find_one(
            Course.course_code == data.course_code
        ) 

        if course is None:
            raise EntityNotFoundError
        
        university = await University.find_one(University.title == course.university_title)

        if university is None:
            raise EntityNotFoundError
        
        if (tutor_info.tutor_name in tutor_info.course_list):
            tutor_info.course_list.remove(course.course_code)

        if (tutor_info.tutor_name in course.tutor_list):
            course.tutor_list.remove(tutor_info.tutor_name)

        if (tutor_info.tutor_name in university.tutor_list):
            university.tutor_list.remove(tutor_info.tutor_name)

        await tutor_info.save()
        await course.save()
        await university.save()

        return utils.create_response(
                status_code=200,
                success=True,
                message="Course removed from tutor successfully.",
                data = ResponseRoleDTO(**tutor_info.model_dump())
            )
    
    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@tutor_router.delete("/deletetutor/{tutorEmail}")
async def deletetutorinfo(tutorEmail:str):
    try:
        tutor = await User.find_one(
                User.email == tutorEmail,
                User.role == UserTypeEnum.TUTOR,
            )
        
        if tutorEmail is None:
            raise EntityNotFoundError
        
        tutor_info = await Tutor.find_one(
            Tutor.tutor_email == tutorEmail,
        )

        if tutor_info is None:
            raise EntityNotFoundError
        
        await tutor.delete()
        await tutor_info.delete()

        return utils.create_response(
                status_code=200,
                success=True,
                message="Tutor deleted successfully.",
            )
    
    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 