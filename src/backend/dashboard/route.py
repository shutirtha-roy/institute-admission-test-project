import base64
from fastapi import APIRouter

from course.model import Course
from error.exception import EntityNotFoundError, UnauthorizedError
from session.model import Session
from university.model import University
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