from enum import Enum
from uuid import UUID
from beanie import Document
from datetime import datetime, timezone

from pydantic import EmailStr
import pymongo


class UserTypeEnum(str, Enum):
    ADMIN = "admin"
    FACULTY = "Faculty"
    STUDENT = "student"

class User(Document):
    password: str
    role: UserTypeEnum
    name: str
    email: str

    # class Settings:
    #     indexes = [
    #         pymongo.IndexModel([
    #             ("email", pymongo.ASCENDING),
    #             ("name", pymongo.ASCENDING),
    #         ], unique=True)
    #     ]