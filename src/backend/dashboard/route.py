from fastapi import APIRouter

from error.exception import EntityNotFoundError, UnauthorizedError
from utils import utils

dashboard_router = APIRouter(tags=["Dashboard"])
