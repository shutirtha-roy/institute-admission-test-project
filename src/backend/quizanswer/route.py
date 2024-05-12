from fastapi import APIRouter

from error.exception import EntityNotFoundError, UnauthorizedError
from student.model import StudentInfo
from utils import utils

from quizanswer.model import QuizAnswer
from quizanswer.dto import ResponseDTO, CreateDTO

quiz_answer_router = APIRouter(tags=["QuizAnswer"])


# @quiz_answer_router.post("/quizAnswerCreate", status_code = 201)  
# async def createuquiz(data: CreateDTO):
#     try:
#         student = await StudentInfo(StudentInfo.find_one())
#         quiz_data = await QuizAnswer.find_one(QuizAnswer.student)
#          = await Tutor.find_one(Tutor.tutor_email == data.tutor_email)
#         if tutor is None:
#             raise EntityNotFoundError
        
#         course = await Course.find_one(Course.course_code == data.course_code)
#         if course is None:
#             raise EntityNotFoundError
        
#         quiz = Quiz(**data.model_dump(), tutor= tutor, course= course)

#         await quiz.save()

#         return utils.create_response(
#             status_code=201,
#             success=True,
#             message="University has been created successfully",
#             data=ResponseDTO(**quiz.model_dump())
#         )
    
#     except EntityNotFoundError as enfe:
#         return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
#     except UnauthorizedError as us:
#         return utils.create_response(status_code=us.status_code, success=False, message=us.message)
#     except Exception as e:
#         return utils.create_response(status_code=500, success=False, message=str(e))