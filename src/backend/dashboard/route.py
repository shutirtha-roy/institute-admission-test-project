from fastapi import APIRouter

from error.exception import EntityNotFoundError, UnauthorizedError
from session.model import Session
from utils import utils

dashboard_router = APIRouter(tags=["Dashboard"])


@dashboard_router.get('/getUniversityDashboard', status_code=200)
async def getallsession():
    try:
        sessions = await Session.find_all().to_list()

        uni_info = {}

        for sesssion in sessions:
            if sesssion.university.title in uni_info.keys():
                uni_info[sesssion.university.title] += len(sesssion.approved_student_list)
            else:
                uni_info.update({sesssion.university.title : len(sesssion.approved_student_list)})

        return utils.create_response(
            status_code=200,
            success=True,
            message="Session List has been retrieved successfully",
            result=uni_info,
        )

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 