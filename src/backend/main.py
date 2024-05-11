from fastapi import FastAPI
from contextlib import asynccontextmanager
from user.route import user_router
from tutor.route import tutor_router
from university.route import university_router
from course.route import course_router
from student.route import student_router
from session.route import session_router
from quiz.route import quiz_router
from database import init_db

# @asynccontextmanager
# async def lifespan(application: FastAPI):
#     await init_db()

app = FastAPI()

@app.on_event("startup")
async def connect():
    await init_db()

app.include_router(user_router, prefix="/api/v1/user")
app.include_router(tutor_router, prefix="/api/v1/tutor")
app.include_router(university_router, prefix="/api/v1/university")
app.include_router(course_router, prefix="/api/v1/course")
app.include_router(student_router, prefix="/api/v1/student")
app.include_router(session_router, prefix="/api/v1/session")
app.include_router(quiz_router, prefix="/api/v1/quiz")