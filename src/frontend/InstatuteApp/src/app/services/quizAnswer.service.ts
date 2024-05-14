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
}
