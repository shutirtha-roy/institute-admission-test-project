from fastapi import APIRouter

from error.exception import EntityNotFoundError, UnauthorizedError
from quiz.model import Quiz, QuizQuesion
from quiz.dto import CreateDTO, AddQuestionDto, DeleteQuestionDto, ResponseDTO
from utils import utils

quiz_router = APIRouter(tags=["Quiz"])

@quiz_router.post("/quizCreate", status_code = 201)  
async def createuquiz(data: CreateDTO):
    try:
        quiz = Quiz(**data.model_dump())

        await quiz.save()

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
    

@quiz_router.get('/allQuiz', status_code=200)
async def getallQuiz():
    try:
        quizes = await Quiz.find_all().to_list()

        if quizes is None:
            raise EntityNotFoundError

        return utils.create_response(
            status_code=200,
            success=True,
            message="Quiz Data has been retrieved successfully",
            result=[ResponseDTO(**r.model_dump()) for r in quizes],
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@quiz_router.patch('/addQuestion/{quiz_id}', status_code=200)
async def addQuestion(quiz_id:str, data: AddQuestionDto):
    try:
        quiz = await Quiz.find_one()

        if quiz is None:
            raise EntityNotFoundError

        quiz_options = data.options.split(",")

        quiz_value = QuizQuesion(
            quiz_question = data.quiz_question,
            options= quiz_options,
            correct_answer = data.correct_answer
        )

        quiz.quiz_questions.update({data.question_number : quiz_value})
        
        await quiz.save()
        
        return utils.create_response(
            status_code=200,
            success=True,
            message="Quiz Data has been retrieved successfully",
            result= ResponseDTO(**quiz.model_dump()),
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 


@quiz_router.delete("/{quiz_id}", status_code = 200)
async def delete(quiz_id:str):
    try: 
        quiz = await Quiz.find_one(
            Quiz.quiz_id == quiz_id
        )

        await quiz.delete()

        return utils.create_response(
            status_code=200,
            success=True,
            message="University has been deleted successfully",
        )
   
    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 