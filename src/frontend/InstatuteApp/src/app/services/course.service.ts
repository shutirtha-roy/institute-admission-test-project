import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class CourseService {
  private baseUrl: string = "/api/v1/course/";

  constructor(
    private http: HttpClient, 
    private router: Router) { 
  }

  getAllCourses() {
    return this.http.get(`${this.baseUrl}getallcourses`);
  }

  deleteCourse(course_code: string) {
    return this.http.delete(`${this.baseUrl}${course_code}`);
  }
}
