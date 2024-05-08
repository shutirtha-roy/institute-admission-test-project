from fastapi import APIRouter

from tutor.dto import CreateDTO, ResponseRoleDTO
from tutor.model import Tutor

tutor_router = APIRouter(tags=["Tutor"])

@tutor_router.patch('/')
async def changestudentinfo():
    pass
