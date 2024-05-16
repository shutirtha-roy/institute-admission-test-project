import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class QuizService {
  private baseUrl: string = "/api/v1/quiz/";

  constructor(
    private http: HttpClient, 
    private router: Router) { 
  }

  createQuiz(quizCreateObj: any) {
    return this.http.post(`${this.baseUrl}quizCreate`, quizCreateObj);
  }

  getAllQuiz() {
    return this.http.get(`${this.baseUrl}allQuiz`);
  }

  getAllQuizByCourse(course_code: string) {
    return this.http.get(`${this.baseUrl}allQuizbyCourse/${course_code}`);
  }

  getAllQuizByTutor(email: string) {
    return this.http.get(`${this.baseUrl}allQuizbyTutor/${email}`);
  }

  getAllQuizByID(quiz_id: string) {
    return this.http.get(`${this.baseUrl}/QuizbyId/${quiz_id}`);
  }

  addQuestionToQuiz(quiz_id: string, question_Obj: any) {
    return this.http.patch(`${this.baseUrl}addQuestion/${quiz_id}`, question_Obj);
  }

  removeQuestionFromQuiz(quiz_id: string, questionNumberObj: any) {
    return this.http.patch(`${this.baseUrl}addQuestion/${quiz_id}`, questionNumberObj);
  }

  deleteQuiz(quiz_id: string) {
    return this.http.delete(`${this.baseUrl}${quiz_id}`);
  }
}
