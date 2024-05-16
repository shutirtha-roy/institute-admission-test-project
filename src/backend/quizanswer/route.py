from ast import Not
from fastapi import APIRouter

from course.model import Course
from error.exception import EntityNotFoundError, UnauthorizedError
from quiz.model import Quiz
from session.model import Session
from student.model import StudentInfo
from utils import utils

from quizanswer.model import QuizAnswer
from quizanswer.dto import CourseResponseDTO, ResponseDTO, CreateDTO, DeleteDTO, StudentEmailDto, StudentGivenQuizDto

quiz_answer_router = APIRouter(tags=["QuizAnswer"])


@quiz_answer_router.post("/quizAnswerCreate", status_code = 201)  
async def createuquiz(data: CreateDTO):
    try:
        quiz_data = await QuizAnswer.find_one(QuizAnswer.student.email==data.student_email, QuizAnswer.quiz_id == data.quiz_id)
        if quiz_data is not None:
            raise Exception("This Student has already given quiz.")

        student = await StudentInfo.find_one(StudentInfo.email == data.student_email)
        if student is None:
            EntityNotFoundError

        quiz = await Quiz.find_one(Quiz.quiz_id == data.quiz_id)
        if quiz is None:
            EntityNotFoundError
        
        quiz_score = 0
        quiz_question_count = len(quiz.quiz_questions.keys())
        all_quiz_answers = data.quiz_answers.split("/")
 
        for quiz_answer in all_quiz_answers:
            qa = quiz_answer.split(",")
            if(quiz.quiz_questions[qa[0]].correct_answer == qa[1]):
                quiz_score += 1
        
        quiz_score_percent = quiz_score/quiz_question_count*100

        quiz_answer_final = QuizAnswer(
            quiz_id = data.quiz_id,
            student = student,
            course= quiz.course,
            description=quiz.description,
            quiz_answers = data.quiz_answers,
            quiz_score = str(quiz_score)+"/"+str(quiz_question_count),
            quiz_score_percent = quiz_score_percent
        )

        await quiz_answer_final.save()

        return utils.create_response(
            status_code=201,
            success=True,
            message="University has been created successfully",
            data=ResponseDTO(**quiz_answer_final.model_dump())
        )
    
    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e))
    

@quiz_answer_router.get('/allQuizAnswer', status_code=200)
async def getallQuizAnswer():
    try:
        quizAnswers = await QuizAnswer.find_all().to_list()

        if quizAnswers is None:
            raise EntityNotFoundError

        return utils.create_response(
            status_code=200,
            success=True,
            message="Quiz Data has been retrieved successfully",
            result=[ResponseDTO(**r.model_dump()) for r in quizAnswers],
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@quiz_answer_router.get('/quizAnswerById/{quiz_id}', status_code=200)
async def getQuizAnswerById(quiz_id:str):
    try:
        quizAnswers = await QuizAnswer.find(QuizAnswer.quiz_id == quiz_id).to_list()

        if quizAnswers is None:
            raise EntityNotFoundError

        return utils.create_response(
            status_code=200,
            success=True,
            message="Quiz Data has been retrieved successfully",
            result=[ResponseDTO(**r.model_dump()) for r in quizAnswers] ,
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@quiz_answer_router.get('/quizAnswerByStudentEmail/{studentEmail}', status_code=200)
async def getQuizAnswerByStudent(studentEmail:str):
    try:
        quizAnswers = await QuizAnswer.find(QuizAnswer.student.email == studentEmail).to_list()

        if quizAnswers is None:
            raise EntityNotFoundError

        return utils.create_response(
            status_code=200,
            success=True,
            message="Quiz Data has been retrieved successfully",
            result=[ResponseDTO(**r.model_dump()) for r in quizAnswers] 
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 


@quiz_answer_router.get('/getCourseQuizByStudentEmail/{course_code}/{student_email}', status_code=200)
async def getCourseQuizByStudentEmail(course_code:str, student_email: str):
    try:
        student = await StudentInfo.find_one(StudentInfo.email == student_email)
        if student is None:
            raise EntityNotFoundError
        
        course = await Course.find_one(Course.course_code == course_code)
        if course is None:
            raise EntityNotFoundError
        
        all_course_quizes = await Quiz.find(Quiz.course == course).to_list()
        given_quiz_answers = await QuizAnswer.find(QuizAnswer.course == course).to_list()
        given_quizes = []
        for given_quiz_answer in given_quiz_answers:
            given_quiz = await Quiz.find_one(Quiz.course == given_quiz_answer.course)
            given_quizes.append(given_quiz)

        return utils.create_response(
            status_code=200,
            success=True,
            message="Quiz Data has been retrieved successfully",
            result=StudentGivenQuizDto(course_quizes = all_course_quizes, given_quizes = given_quizes)
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@quiz_answer_router.delete('/deletequizAnswer', status_code=200)
async def deleteQuizAnswer(data:DeleteDTO):
    try:
        quiz_data = await QuizAnswer.find_one(QuizAnswer.student.email==data.student_email, QuizAnswer.quiz_id == data.quiz_id)

        if quiz_data is None:
            raise EntityNotFoundError
        
        await quiz_data.delete()

        return utils.create_response(
            status_code=200,
            success=True,
            message="Quiz Data has been deleted successfully"
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 