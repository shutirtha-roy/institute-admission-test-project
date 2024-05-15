from fastapi import APIRouter

from error.exception import EntityNotFoundError, UnauthorizedError
from session.model import Session
from student.model import StudentInfo
from student.dto import ResponseDTO
from user.model import User, UserTypeEnum
from utils import utils

student_router = APIRouter(tags=["Student"])


@student_router.get('/allstudent', status_code=200)
async def getallstudent():
    try:
        students = await StudentInfo.find_all().to_list()

        if students is None:
            raise EntityNotFoundError

        responses = []

        for student in students:
            print(student)
            sessions = []
            courses = []
            universities = []
            
            for session_id in student.sessions:
                session = await Session.find_one(Session.session_id == session_id)
                sessions.append(session)
                
                if session.course not in courses:
                    courses.append(session.course)

                if session.university not in universities:
                    universities.append(session.university)

            response = ResponseDTO(
                email= student.email, 
                name= student.name,
                sessions= sessions,
                university= universities,
                courses=courses)
            
            responses.append(response)

        return utils.create_response(
            status_code=200,
            success=True,
            message="Tutor List has been retrieved successfully",
            result=responses,
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@student_router.get('/getOneStudent/{stident_email}', status_code=200)
async def getallstudent(stident_email:str):
    try:
        student = await StudentInfo.find_one(StudentInfo.email == stident_email)

        if student is None:
            raise EntityNotFoundError

        sessions = []
        universities = []
        courses = []

        for session_id in student.sessions:
            session = await Session.find_one(Session.session_id == session_id)
            sessions.append(session)
            
            if session.course not in courses:
                courses.append(session.course)

            if session.university not in universities:
                universities.append(session.university)

        return utils.create_response(
            status_code=200,
            success=True,
            message="Tutor List has been retrieved successfully",
            result=ResponseDTO(
                email= student.email, 
                name= student.name,
                sessions= sessions,
                university= universities,
                courses=courses),
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@student_router.delete("/deletestudent/{studentEmail}")
async def deletetutorinfo(studentEmail:str):
    try:
        student = await User.find_one(
                User.email == studentEmail,
                User.role == UserTypeEnum.STUDENT,
            )

        if studentEmail is None:
            raise EntityNotFoundError
        
        Student_info = await StudentInfo.find_one(
            StudentInfo.email == studentEmail,
        )

        if Student_info is None:
            raise EntityNotFoundError
        
        await student.delete()
        await Student_info.delete()

        return utils.create_response(
                status_code=200,
                success=True,
                message="Student deleted successfully.",
            )
    
    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 