import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class QuizAnswerService {
  private baseUrl: string = "/api/v1/quizAnswer/";

  constructor(
    private http: HttpClient, 
    private router: Router) { 
  }

  createQuizAnswer(quizAnswerCreateObj: any) {
    return this.http.post(`${this.baseUrl}quizAnswerCreate`, quizAnswerCreateObj);
  }

  getAllQuizAnswer() {
    return this.http.get(`${this.baseUrl}allQuizAnswer`);
  }

  getQuizAnswerByStudentEmail(email: string) {
    return this.http.get(`${this.baseUrl}quizAnswerByStudentEmail/${email}`);
  }

  getQuizAnswerById(quiz_id: string) {
    return this.http.get(`${this.baseUrl}quizAnswerById/${quiz_id}`);
  }

  getCourseQuizByStudentEmail(course_code: string, studentEmail: string) {
    return this.http.get(`${this.baseUrl}getCourseQuizByStudentEmail/${course_code}/${studentEmail}`);
  }
}
