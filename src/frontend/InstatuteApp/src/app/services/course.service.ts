import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class CourseService {
  private baseUrl: string = "/api/v1/course/";
  private tutorUrl: string = "/api/v1/tutor/";

  constructor(
    private http: HttpClient, 
    private router: Router) { 
  }

  getAllCourses() {
    return this.http.get(`${this.baseUrl}getallcourses`);
  }

  createCourse(courseObj: any) {
    return this.http.post(`${this.baseUrl}courseCreate`, courseObj);
  }

  assignTutorToCourse(email: string, courseCodeObj: any) {
    return this.http.patch(`${this.tutorUrl}addtutorcourse/${email}`, courseCodeObj);
  }

  deleteCourse(course_code: string) {
    return this.http.delete(`${this.baseUrl}${course_code}`);
  }
}
