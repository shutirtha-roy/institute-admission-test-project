from fastapi import FastAPI
from contextlib import asynccontextmanager
from user.route import user_router
from faculty.route import faculty_router
from database import init_db

# @asynccontextmanager
# async def lifespan(application: FastAPI):
#     await init_db()

app = FastAPI()

@app.on_event("startup")
async def connect():
    await init_db()

app.include_router(user_router, prefix="/api/v1/user")
app.include_router(faculty_router, prefix="/api/v1/faculty")