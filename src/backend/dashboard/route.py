import base64
from fastapi import APIRouter

from course.model import Course
from error.exception import EntityNotFoundError, UnauthorizedError
from quiz.model import Quiz
from quizanswer.model import QuizAnswer
from session.model import Session
from student.model import StudentInfo
from tutor.model import Tutor
from university.model import University

from dashboard.dto import AdminDashboardDto, StudentEmailDto

from utils import utils
import matplotlib.pyplot as plt
import io

dashboard_router = APIRouter(tags=["Dashboard"])


@dashboard_router.get('/getUniversityDashboard', status_code=200)
async def getallsession():
    try:
        sessions = await Session.find_all().to_list()
        tutor_number =  len(await Tutor.find_all().to_list())
        student_number = len(await StudentInfo.find_all().to_list())

        uni_info = {}

        for sesssion in sessions:
            if sesssion.university.title in uni_info.keys():
                uni_info[sesssion.university.title] += len(sesssion.approved_student_list)
            else:
                uni_info.update({sesssion.university.title : len(sesssion.approved_student_list)})

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
            result=AdminDashboardDto(
                number_of_students= student_number,
                number_of_tutors= tutor_number,
                my_base64_jpgData =my_base64_jpgData
            ),
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
            uni_info.update({course.title : 0})

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
    

@dashboard_router.get('/getStudentCourseDashboard/{student_email}', status_code=200)
async def getallsession(student_email:str):
    try:
        student = await StudentInfo.find_one(StudentInfo.email == student_email)

        if student is None:
            raise EntityNotFoundError

        sessions = []
        universities = []
        courses = []

        for session_id in student.sessions:
            session = await Session.find_one(Session.session_id == session_id)
            sessions.append(session)
            
            if session.course not in courses:
                courses.append(session.course)

            if session.university not in universities:
                universities.append(session.university)

        courses_info = {}

        for course in courses:
            all_course_quizes = await Quiz.find(Quiz.course == course).to_list()
            given_quiz_answers = await QuizAnswer.find(QuizAnswer.course == course, QuizAnswer.student.email == student_email).to_list()
            
            given_quizes = []
            for given_quiz_answer in given_quiz_answers:
                given_quiz = await Quiz.find_one(Quiz.quiz_id == given_quiz_answer.quiz_id)
                given_quizes.append(given_quiz)

            course_quizes_number = len(all_course_quizes)
            given_quiz_number = len(given_quizes)

            percentage_given = given_quiz_number/course_quizes_number*100

            courses_info.update({course.title : percentage_given})

        courses = list(courses_info.keys())
        values = list(courses_info.values())
        
        fig = plt.figure(figsize = (10, 5))
        plt.bar(courses, values, color ='maroon', 
                width = 0.4)
        
        plt.xlabel("Courses")
        plt.ylabel("Course Quiz Completation")
        plt.title("Status of students Course Completation by Given Quiz")

        my_stringIObytes = io.BytesIO()
        plt.savefig(my_stringIObytes, format='jpg')
        my_stringIObytes.seek(0)
        my_base64_jpgData = base64.b64encode(my_stringIObytes.read()).decode()

        return utils.create_response(
            status_code=200,
            success=True,
            message="Student Data has been retrieved successfully",
            result=my_base64_jpgData
        ) 

    except EntityNotFoundError as enfe:
        return utils.create_response(status_code=enfe.status_code, success=False, message=enfe.message)    
    except UnauthorizedError as us:
        return utils.create_response(status_code=us.status_code, success=False, message=us.message)
    except Exception as e:
        return utils.create_response(status_code=500, success=False, message=str(e)) 