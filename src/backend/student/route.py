from fastapi import APIRouter

from error.exception import EntityNotFoundError, UnauthorizedError
from student.model import StudentInfo
from student.dto import ResponseDTO
from utils import utils

student_router = APIRouter(tags=["Student"])


@student_router.get('/allstudent', status_code=200)
async def getallstudent():
    try:
        students = await StudentInfo.find_all().to_list()

        if students is None:
            raise EntityNotFoundError

        return utils.create_response(
            status_code=200,
            success=True,
            message="Tutor List has been retrieved successfully",
            result=[ResponseDTO(**r.model_dump()) for r in students],
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 