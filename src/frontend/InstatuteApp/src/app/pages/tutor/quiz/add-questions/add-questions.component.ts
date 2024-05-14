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
  questionForm!: FormGroup;
  questionId: string | null = "";
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
    this.questionForm = this.formBuilder.group({
      quiz_question: ['', Validators.required],
      optionOne: ['', Validators.required],
      optionTwo: ['', Validators.required],
      optionThree: ['', Validators.required],
      optionFour: ['', Validators.required],
      correct_answer: ['', Validators.required]
    });

    this.getQuestionDetails();
  }

  getQuestionDetails() {
    this.route.paramMap.subscribe({
      next: (params) => {
        this.questionId = params.get('quiz_id');

        if (this.questionId) {
          this.quizService.getAllQuizByID(this.questionId)
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

  onQuestionSubmit() {
    this.submitted = true;

    if(this.questionForm.valid) {
      console.log("QUESTION IS HERE", this.questionId);
    }
  }
}
