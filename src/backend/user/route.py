from datetime import datetime
from uuid import UUID
import bcrypt
from fastapi import APIRouter

from error.exception import EntityNotFoundError, UnauthorizedError
from middleware.authentication.hash import create_access_token
from user.dto import CreateUserDTO, CreateUserDTO, LoginUserDTO, ResponseUserDTO, StudentListResponseDTO
from user.model import User, UserTypeEnum
from utils import utils

user_router = APIRouter()

@user_router.get('/', status_code=200)
async def getallusers():
    users = await User.find_all().to_list() 
    return users

@user_router.get('/students', status_code=200)
async def getallstudents():
    try:
        students = await User.find(User.role == UserTypeEnum.STUDENT).to_list() 
        student_number = len(students)

        return utils.create_response(
            status_code=200,
            success=True,
            message="Student List has been retrieved successfully",
            data={
                "user": StudentListResponseDTO(
                    total_students=student_number,
                    studentt_list=students
                    ),
            }
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

@user_router.get('/tutors', status_code=200)
async def getalltutors():
    tutors = await User.find(User.role == UserTypeEnum.TUTOR).to_list() 
    return tutors

@user_router.get('/{task_id}')
async def getonestudent(task_id):
    pass

@user_router.post("/login", status_code=200)
async def login_user(data: LoginUserDTO):
    try:
        user = await User.find_one(User.email == data.email)

        if user is None or user.password is data.password:
            raise UnauthorizedError

        if user.approved is False:
            raise Exception("Account has not been approved.")

        access_token = create_access_token(user.name, user.email, user.role.value)

        await user.save()
        
        return utils.create_response(
            status_code=200,
            success=True,
            message="User has logged in successfully",
            data={
                "user": ResponseUserDTO(**user.dict()).dict(),
                "access_token": access_token
            }
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
    

@user_router.post("/studentcreate", status_code=201)
async def createstudent(data: CreateUserDTO):

    student = User(
        name= data.name,
        email= data.email,
        password= bcrypt.hashpw(
            data.password.encode("utf-8"), bcrypt.gensalt()),
        role= UserTypeEnum.STUDENT,
        approved = False
    )

    await student.save()
    
    return {"massege" : "Resquest for account created successfully."}

@user_router.post("/tutorcreate", status_code=201)
async def createstudent(data: CreateUserDTO):
    tutor = User(
        name= data.name,
        email= data.email,
        password= data.password,
        role= UserTypeEnum.TUTOR,
        approved= True
    )

    await tutor.save()
    
    return {"massege" : "Tutor Created successfully"}


@user_router.patch('/')
async def changestudentinfo():
    pass


@user_router.patch("/approveStudent/{studentEmail}")
async def approveStudent(studentEmail:str):
    try:
        student = await User.find_one(
                User.email == studentEmail,
                User.role == UserTypeEnum.STUDENT,
            )

        if student is None:
            raise EntityNotFoundError
        
        student.approved = True

        await student.save()

        return utils.create_response(
                status_code=200,
                success=True,
                message="Student account approved successfully.",
            )
    
    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 


@user_router.delete("/{userEmail}", status_code = 200)
async def delete(userEmail:str):
    try: 
        user = await User.find_one(
            User.email == userEmail
        )
        
        await user.delete()

        return utils.create_response(
            status_code=200,
            success=True,
            message="User has been deleted successfully",
        )
   
    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 