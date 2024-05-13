from ast import Not
from fastapi import APIRouter

from error.exception import EntityNotFoundError, UnauthorizedError
from quiz.model import Quiz
from student.model import StudentInfo
from utils import utils

from quizanswer.model import QuizAnswer
from quizanswer.dto import ResponseDTO, CreateDTO

quiz_answer_router = APIRouter(tags=["QuizAnswer"])


@quiz_answer_router.post("/quizAnswerCreate", status_code = 201)  
async def createuquiz(data: CreateDTO):
    try:
        quiz_data = await QuizAnswer.find_one(QuizAnswer.student==data.student_email, QuizAnswer.quiz_id == data.quiz_id)

        if quiz_data is not None:
            raise Exception("This Student has already given quiz.")
        
        student = await StudentInfo(StudentInfo.find_one())
        if student is None:
            EntityNotFoundError

        quiz = await Quiz.find_one(Quiz.quiz_id == data.quiz_id)
        if quiz is None:
            EntityNotFoundError
        
        for qa in data.quiz_answers.keys():
            quiz_answers = quiz.quiz_questions
            print(qa)
            print(quiz_answers[qa])
        
        
        # await quiz.save()

        return utils.create_response(
            status_code=201,
            success=True,
            message="University has been created successfully",
            data=ResponseDTO(**quiz.model_dump())
        )
    
    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e))