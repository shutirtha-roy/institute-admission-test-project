from datetime import datetime
from uuid import UUID
from fastapi import APIRouter

from course.model import Course
from error.exception import EntityNotFoundError, UnauthorizedError
from session.dto import CreateDTO, ResponseDTO, UpdateDTO, UpdateStudentListDTO
from session.model import Session
from student.model import StudentInfo
from tutor.model import Tutor
from university.model import University
from utils import utils

session_router = APIRouter(tags=["Session"])

@session_router.post("/sessionCreate", status_code = 201)  
async def createsession(data: CreateDTO):
    try:
        tutor = await Tutor.find_one(Tutor.tutor_email == data.host_email)
        if tutor is None:
            raise EntityNotFoundError()
        
        course = await Course.find_one(Course.course_code == data.course_code)
        if course is None:
            raise EntityNotFoundError()
        
        university = await University.find_one(University.title == course.university_title)
        if university is None:
            raise EntityNotFoundError()
        
        session = Session(**data.model_dump(), tutor=tutor, course=course, university=university)

        await session.save()

        return utils.create_response(
            status_code=201,
            success=True,
            message="Course has been created successfully",
            data=ResponseDTO(**session.model_dump())
        )
    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    
    except EntityNotFoundError as en:
        return utils.create_response(status_code=en.status_code, success=False, message=en.message)
    
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e))
    

@session_router.get('/getsession/{session_id}', status_code=200)
async def getallsession(session_id:str):
    try:
        session = await Session.find_one(
            Session.session_id == session_id
        )

        if session is None:
            raise EntityNotFoundError

        return utils.create_response(
            status_code=200,
            success=True,
            message="Session has been retrieved successfully",
            result=ResponseDTO(**session.model_dump()),
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
    

@session_router.get('/getallsession', status_code=200)
async def getallsession():
    try:
        sessions = await Session.find_all().to_list()

        return utils.create_response(
            status_code=200,
            success=True,
            message="Session List has been retrieved successfully",
            result=[ResponseDTO(**r.model_dump()) for r in sessions],
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


@session_router.get('/getallsessionbytutor/{tutor_email}', status_code=200)
async def getallsessionbytutor(tutor_email: str):
    try:
        sessions = await Session.find(Session.tutor.tutor_email == tutor_email).to_list()

        if sessions is None:
            raise EntityNotFoundError

        return utils.create_response(
            status_code=200,
            success=True,
            message="Session List has been retrieved successfully",
            result=[ResponseDTO(**r.model_dump()) for r in sessions],
        )

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 


@session_router.patch('/updatesession/{session_id}', status_code=200)
async def updatesession(session_id:str, data: UpdateDTO):
    try:
        session = await Session.find_one(
            Session.session_id == session_id
        )

        if session is None:
            raise EntityNotFoundError
        
        if(data.session_id):
            session.session_id = data.session_id

        if(data.description):
            session.description = data.description

        if(data.student_number):
            session.student_number = data.student_number

        session.save()

        return utils.create_response(
            status_code=200,
            success=True,
            message="Session Updated successfully",
            result= ResponseDTO(**session.model_dump()),
        )

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 


@session_router.patch('/addstudent/{session_id}', status_code=200)
async def addstudenttosession(session_id:str, data: UpdateStudentListDTO):
    try:
        session = await Session.find_one(
            Session.session_id == session_id
        )

        if session is None:
            raise EntityNotFoundError

        student = await StudentInfo.find_one(StudentInfo.email == data.student_email)

        if student is None:
            raise EntityNotFoundError

        if(student in session.unapproved_student_list):
            raise Exception("Request For Student Approval Already Made")

        session.unapproved_student_list.append(student)

        await session.save()

        return utils.create_response(
            status_code=200,
            success=True,
            message="Session Updated successfully",
            result= ResponseDTO(**session.model_dump()),
        )

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@session_router.patch('/approvestudent/{session_id}', status_code=200)
async def approvestudenttosession(session_id:str, data: UpdateStudentListDTO):
    try:
        session = await Session.find_one(Session.session_id == session_id)
        if session is None:
            raise EntityNotFoundError
        
        student = await StudentInfo.find_one(StudentInfo.email == data.student_email)
        if student is None:
            raise EntityNotFoundError
        
        unapproved_student_emails = [] 
        
        for unapproved_student in session.unapproved_student_list:
            unapproved_student_emails = unapproved_student.email
        
        if(student.email in unapproved_student_emails):
            for unapproved_student_info in session.unapproved_student_list:
                if (unapproved_student_info.email == data.student_email):
                    session.unapproved_student_list.remove(student)
            session.approved_student_list.append(student)
            student.sessions.append(session.session_id)

        await session.save()
        await student.save()

        return utils.create_response(
            status_code=200,
            success=True,
            message="Session Updated successfully",
            result= ResponseDTO(**session.model_dump()),
        )

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 


@session_router.patch('/upapprovestudent/{session_id}', status_code=200)
async def approvestudenttosession(session_id:str, data: UpdateStudentListDTO):
    try:
        session = await Session.find_one(Session.session_id == session_id)
        if session is None:
            raise EntityNotFoundError
        
        student = await StudentInfo.find_one(StudentInfo.email == data.student_email)
        if student is None:
            raise EntityNotFoundError
        
        if(student in session.approved_student_list):
            session.unapproved_student_list.append(student)
            session.approved_student_list.remove(student)
            student.sessions.remove(session.session_id)
            
        await session.save()
        await student.save()

        return utils.create_response(
            status_code=200,
            success=True,
            message="Session Updated successfully",
            result= ResponseDTO(**session.model_dump()),
        )

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 


@session_router.patch('/deletestudent/{session_id}', status_code=200)
async def deletestudenttosession(session_id:str, data: UpdateStudentListDTO):
    try:
        session = await Session.find_one(Session.session_id == session_id)
        if session is None:
            raise EntityNotFoundError
        
        student = await StudentInfo.find_one(StudentInfo.email == data.student_email)
        if student is None:
            raise EntityNotFoundError
        
        if(student in session.approved_student_list):
            session.approved_student_list.remove(student)
            student.sessions.remove(session.session_id)
            
        await session.save()
        await student.save()

        return utils.create_response(
            status_code=200,
            success=True,
            message="Session Updated successfully",
            result= ResponseDTO(**session.model_dump()),
        )

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@session_router.delete("/{session_id}", status_code = 200)
async def delete(session_id:str):
    try: 
        session = await Session.find_one(
            Session.session_id == session_id
        )

        if session is None:
            raise EntityNotFoundError
        
        await session.delete()

        return utils.create_response(
            status_code=200,
            success=True,
            message="Session has been deleted successfully",
        )
   
    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 