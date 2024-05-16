import base64
from fastapi import APIRouter

from course.model import Course
from error.exception import EntityNotFoundError, UnauthorizedError
from quiz.model import Quiz, QuizQuesion
from quiz.dto import CreateDTO, AddQuestionDto, DeleteQuestionDto, ResponseDTO, QuizQuestionResponseDTO
from tutor.model import Tutor
from utils import utils
import matplotlib.pyplot as plt
import io

quiz_router = APIRouter(tags=["Quiz"])

@quiz_router.post("/quizCreate", status_code = 201)  
async def createuquiz(data: CreateDTO):
    try:
        tutor = await Tutor.find_one(Tutor.tutor_email == data.tutor_email)
        if tutor is None:
            raise EntityNotFoundError
        course = await Course.find_one(Course.course_code == data.course_code)
        if course is None:
            raise EntityNotFoundError
        quiz = Quiz(**data.model_dump(), tutor= tutor, course= course)
        await quiz.save()

        return utils.create_response(
            status_code=201,
            success=True,
            message="Course has been created successfully",
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

        # x = [1,2,3]
        # y = [2,4,1]
        # plt.plot(x, y)
        # plt.xlabel('x - axis')
        # plt.ylabel('y - axis')
        # plt.title('My first graph!')
        # my_stringIObytes = io.BytesIO()
        # plt.savefig(my_stringIObytes, format='jpg')
        # my_stringIObytes.seek(0)
        # my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()

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


@quiz_router.get('/QuizbyId/{quiz_id}', status_code=200)
async def getaQuizbyId(quiz_id:str):
    try:
        quiz = await Quiz.find_one(Quiz.quiz_id == quiz_id)

        if quiz is None:
            raise EntityNotFoundError

        question_list = []
        question_numbers = quiz.quiz_questions.keys()

        for question_number in question_numbers:
            quiz_question = quiz.quiz_questions[question_number]

            show_ques = QuizQuestionResponseDTO(
                **quiz_question.model_dump(),
                question_number=question_number
            )
            question_list.append(show_ques)

        return utils.create_response(
            status_code=200,
            success=True,
            message="Quiz Data has been retrieved successfully",
            result=question_list,
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 


@quiz_router.get('/allQuizbyCourse/{course_code}', status_code=200)
async def getallQuizbyCourse(course_code:str):
    try:
        quizes = await Quiz.find(Quiz.course.course_code == course_code).to_list()

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


@quiz_router.get('/allQuizbyTutor/{tutor_email}', status_code=200)
async def getallQuizbyTutor(tutor_email:str):
    try:
        quizes = await Quiz.find(Quiz.tutor.tutor_email == tutor_email).to_list()

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
        quiz = await Quiz.find_one(Quiz.quiz_id == quiz_id)

        if quiz is None:
            raise EntityNotFoundError

        quiz_options = data.options.split(",")

        quiz_value = QuizQuesion(
            quiz_question = data.quiz_question,
            options= quiz_options,
            correct_answer = data.correct_answer
        )

        quiz_question_numbers = quiz.quiz_questions.keys()

        if data.question_number in quiz_question_numbers:
            raise Exception("Question number already in quiz.")

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


@quiz_router.patch('/removeQuestion/{quiz_id}', status_code=200)
async def addQuestion(quiz_id:str, data: DeleteQuestionDto):
    try:
        quiz = await Quiz.find_one(Quiz.quiz_id == quiz_id)

        if quiz is None:
            raise EntityNotFoundError

        quiz.quiz_questions.pop(data.question_number)
        
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