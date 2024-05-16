import base64
from fastapi import APIRouter

from course.model import Course
from error.exception import EntityNotFoundError, UnauthorizedError
from quiz.model import Quiz
from quizanswer.model import QuizAnswer
from session.model import Session
from student.model import StudentInfo
from university.model import University

from dashboard.dto import StudentEmailDto

from utils import utils
import matplotlib.pyplot as plt
import io

dashboard_router = APIRouter(tags=["Dashboard"])


@dashboard_router.get('/getUniversityDashboard', status_code=200)
async def getallsession():
    try:
        sessions = await Session.find_all().to_list()

        uni_info = {}

        for sesssion in sessions:
            if sesssion.university.title in uni_info.keys():
                uni_info[sesssion.university.title] += len(sesssion.approved_student_list)
            else:
                uni_info.update({sesssion.university.title : len(sesssion.approved_student_list)})

        print(uni_info)
        courses = list(uni_info.keys())
        values = list(uni_info.values())
        
        fig = plt.figure(figsize = (10, 5))
        plt.bar(courses, values, color ='maroon', 
                width = 0.4)
        
        plt.xlabel("Universities")
        plt.ylabel("No. of students enrolled in various courses")
        plt.title("Students enrolled in different courses of the Universities")

        my_stringIObytes = io.BytesIO()
        plt.savefig(my_stringIObytes, format='jpg')
        my_stringIObytes.seek(0)
        my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()

        return utils.create_response(
            status_code=200,
            success=True,
            message="University Dashboard has been retrieved successfully",
            result=my_base64_jpgData,
        )

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@dashboard_router.get('/getUniversityCourseDashboard/{university_title}', status_code=200)
async def getallsession(university_title:str):
    try:
        
        courses = await Course.find(Course.university_title == university_title).to_list()

        sessions = await Session.find_all().to_list()
        uni_info = {}

        for course in courses:
            uni_info.update({course.course_code : 0})

        for sesssion in sessions:
            if sesssion.course.course_code in uni_info.keys():
                uni_info[sesssion.course.course_code] += len(sesssion.approved_student_list)

        courses = list(uni_info.keys())
        values = list(uni_info.values())
        
        fig = plt.figure(figsize = (10, 5))
        plt.bar(courses, values, color ='maroon', 
                width = 0.4)
        
        plt.xlabel("Courses")
        plt.ylabel("No. of students enrolled in various courses")
        plt.title("Students enrolled in different courses")

        my_stringIObytes = io.BytesIO()
        plt.savefig(my_stringIObytes, format='jpg')
        my_stringIObytes.seek(0)
        my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()

        return utils.create_response(
            status_code=200,
            success=True,
            message="University Dashboard has been retrieved successfully",
            result=my_base64_jpgData,
        )

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@dashboard_router.get('/getUniversityCourseDashboard/{university_title}', status_code=200)
async def getallsession(university_title:str):
    try:
        
        courses = await Course.find(Course.university_title == university_title).to_list()

        sessions = await Session.find_all().to_list()
        uni_info = {}

        for course in courses:
            uni_info.update({course.course_code : 0})

        for sesssion in sessions:
            if sesssion.course.course_code in uni_info.keys():
                uni_info[sesssion.course.course_code] += len(sesssion.approved_student_list)

        courses = list(uni_info.keys())
        values = list(uni_info.values())
        
        fig = plt.figure(figsize = (10, 5))
        plt.bar(courses, values, color ='maroon', 
                width = 0.4)
        
        plt.xlabel("Courses")
        plt.ylabel("No. of students enrolled in various courses")
        plt.title("Students enrolled in different courses")

        my_stringIObytes = io.BytesIO()
        plt.savefig(my_stringIObytes, format='jpg')
        my_stringIObytes.seek(0)
        my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()

        return utils.create_response(
            status_code=200,
            success=True,
            message="University Dashboard has been retrieved successfully",
            result=my_base64_jpgData,
        )

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 
    

@dashboard_router.get('/getStudentCourseDashboard/{course_code}', status_code=200)
async def getallsession(course_code:str, data:StudentEmailDto):
    try:
        student = await StudentInfo.find_one(StudentInfo.email == data.student_email)
        if student is None:
            raise EntityNotFoundError
        
        course = await Course.find_one(Course.course_code == course_code)
        if course is None:
            raise EntityNotFoundError
        
        all_course_quizes = await Quiz.find(Quiz.course == course).to_list()
        given_quiz_answers = await QuizAnswer.find(QuizAnswer.course == course).to_list()
        quiz_Scores = []
        for given_quiz_answer in given_quiz_answers:
            given_quiz = await Quiz.find_one(Quiz.course == given_quiz_answer.course)
            quiz_Scores.append(given_quiz)

        return utils.create_response(
            status_code=200,
            success=True,
            message="Quiz Data has been retrieved successfully",
            result = "123"
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 