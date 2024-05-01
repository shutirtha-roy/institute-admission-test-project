from datetime import datetime
from uuid import UUID
import bcrypt
from fastapi import APIRouter

from error.exception import EntityNotFoundError, UnauthorizedError
from middleware.authentication.hash import create_access_token
from user.dto import CreateUserDTO, CreateUserDTO, LoginUserDTO, ResponseUserDTO
from user.model import User, UserTypeEnum
from utils import utils

user_router = APIRouter()

@user_router.get('/', status_code=200)
async def getallstudents():
    # User.role == UserTypeEnum.STUDENT
    students = await User.find_all().to_list() 
    return students

@user_router.get('/{task_id}')
async def getonestudent(task_id):
    pass

@user_router.post("/login", status_code=200)
async def login_user(data: LoginUserDTO):
    try:
        user = await User.find_one(User.email == data.email)

        if user is None:
            raise UnauthorizedError

        if data.email is not None and not bcrypt.checkpw(data.password.encode("utf-8"), user.password.encode("utf-8")):
            raise UnauthorizedError

        access_token = create_access_token(user.id)

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
    print(data.name)
    print(data.email)
    print(bcrypt.hashpw(
            data.password.encode("utf-8"), bcrypt.gensalt()))
    print(UserTypeEnum.STUDENT)
    student = User(
        name= data.name,
        email= data.email,
        password= bcrypt.hashpw(
            data.password.encode("utf-8"), bcrypt.gensalt()),
        role= UserTypeEnum.STUDENT
    )
    print("123")
    await student.save()
    
    return {"massege" : "Student Created successfully"}

@user_router.post("/facultycreate", status_code=201)
async def createstudent(data: CreateUserDTO):
    student = User(
        student_name= data.student_name,
        gender= data.gender,
        date_created= data.date_created
    )

    await student.save()
    
    return {"massege" : "Student Created successfully"}

@user_router.patch('/')
async def changestudentinfo():
    pass

@user_router.delete('deletestudent/{user_role_id}')
async def deletestudent():
    pass

@user_router.delete("/{userName}", status_code = 200)
async def delete(userName:str):
    try: 
        print(userName)
        user = await User.find_one(
            User.name == userName
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