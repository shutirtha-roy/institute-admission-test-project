import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { QuizService } from 'src/app/services/quiz.service';
import { SessionService } from 'src/app/services/session.service';
import { UserStoreService } from 'src/app/services/user-store.service';

@Component({
  selector: 'app-quiz',
  templateUrl: './quiz.component.html',
  styleUrls: ['./quiz.component.css']
})
export class QuizComponent implements OnInit {
  quizList!: any[];

  constructor(
    private authService: AuthService,
    private quizService: QuizService) { 

  }

  ngOnInit(): void {
    this.getAllQuizesByTutor();
  }

  getAllQuizesByTutor() {
    const email: string = this.authService.getEmail() ?? "";

    this.quizService.getAllQuizByTutor(email)
      .subscribe({
        next: (response: any) => {
          this.quizList = response.result;
          console.log(response.result);
        },
        error: (response) => {
          console.log(response)
        }
    });
  }
}
