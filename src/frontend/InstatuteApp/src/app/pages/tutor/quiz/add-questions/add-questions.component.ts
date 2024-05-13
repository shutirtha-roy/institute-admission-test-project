import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';
import { QuizService } from 'src/app/services/quiz.service';
import { SessionService } from 'src/app/services/session.service';

@Component({
  selector: 'app-add-questions',
  templateUrl: './add-questions.component.html',
  styleUrls: ['./add-questions.component.css']
})
export class AddQuestionsComponent implements OnInit  {
  session!: any;
  question_list: any[] = [];
  submitted: boolean = false;

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
    this.getQuestionDetails();
  }

  getQuestionDetails() {
    this.route.paramMap.subscribe({
      next: (params) => {
        const questionId = params.get('quiz_id');

        if (questionId) {
          this.quizService.getAllQuizByID(questionId)
          .subscribe({
            next: (response: any) => {
              console.log(response);
              this.question_list = response.result;
              console.log(this.session);
            }
          });
        }
      }
    })
  }
}
