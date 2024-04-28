from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks import student_router
from faculty.route import faculty_router
from database import init_db

# @asynccontextmanager
# async def lifespan(application: FastAPI):
#     await init_db()

app = FastAPI()

@app.on_event("startup")
async def connect():
    await init_db()

app.include_router(student_router, prefix="/students")
app.include_router(faculty_router, prefix="/faculty")