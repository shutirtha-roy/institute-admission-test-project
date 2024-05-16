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
  quizId: string | null = "";
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
      question_number: ['', Validators.required],
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

  onQuestionSubmit() {
    this.submitted = true;

    if(this.questionForm.valid) {
      let optionOne = this.questionForm.value?.optionOne.trim();
      let optionTwo = this.questionForm.value?.optionTwo.trim();
      let optionThree = this.questionForm.value?.optionThree.trim();
      let optionFour = this.questionForm.value?.optionFour.trim();
      let options = `${optionOne},${optionTwo},${optionThree},${optionFour}`;

      let quizDetails = { 'question_number': this.questionForm.value?.question_number, 
        'quiz_question': this.questionForm.value?.quiz_question.trim(),
        'options': options,
        'correct_answer': this.questionForm.value?.correct_answer
      };

      this.quizService.addQuestionToQuiz(this.quizId ?? "", quizDetails)
      .subscribe({
        next: (res) => {
          this.toastr.success("Question Added Successfully");
          console.log(res);
          this.questionForm.reset();
          this.ngOnInit();
        },
        error: (err) => {
          alert(err?.err.message)
        }
      });
    }
  }
}
