import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';
import { QuizService } from 'src/app/services/quiz.service';
import { SessionService } from 'src/app/services/session.service';

@Component({
  selector: 'app-student-answers',
  templateUrl: './student-answers.component.html',
  styleUrls: ['./student-answers.component.css']
})
export class StudentAnswersComponent implements OnInit  {
  question_list: any[] = [];
  quizId: string | null = "";

  constructor(
    private route: ActivatedRoute, 
    private authService: AuthService,
    private sessionService: SessionService, 
    private quizService: QuizService,
    private router: Router,
    private formBuilder: FormBuilder,
    private toastr: ToastrService) { 

  }

  ngOnInit(): void {
    this.getQuestionAnswerDetails();
  }

  getQuestionAnswerDetails() {
    this.route.paramMap.subscribe({
      next: (params) => {
        this.quizId = params.get('quiz_id');

        if (this.quizId) {
          this.quizService.getAllQuizByID(this.quizId)
          .subscribe({
            next: (response: any) => {
              console.log(response);
              this.question_list = response.result;
              console.log(this.question_list);
            }
          });
        }
      }
    })
  }
}
