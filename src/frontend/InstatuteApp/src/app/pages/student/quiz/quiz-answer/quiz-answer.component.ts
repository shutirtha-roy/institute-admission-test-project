import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';
import { QuizService } from 'src/app/services/quiz.service';
import { SessionService } from 'src/app/services/session.service';

@Component({
  selector: 'app-quiz-answer',
  templateUrl: './quiz-answer.component.html',
  styleUrls: ['./quiz-answer.component.css']
})
export class QuizAnswerComponent implements OnInit {
  questionList!: any[];
  quiz_id: string | null = "";
  count: number = 0;
  questionForm!: FormGroup;
  answers!: string;

  constructor(
    private authService: AuthService,
    private sessionService: SessionService,
    private quizService: QuizService,
    private route: ActivatedRoute,
    private router: Router,
    private formBuilder: FormBuilder,
    private toastr: ToastrService) { 

  }

  ngOnInit(): void {
    this.questionForm = this.formBuilder.group({
      answer: ['', Validators.required],
    });

    this.getAllQuestionsByQuiz();
  }

  getAllQuestionsByQuiz() {
    this.route.paramMap.subscribe({
      next: (params) => {
        this.quiz_id = params.get('quiz_id');

        if (this.quiz_id) {
          this.quizService.getAllQuizByID(this.quiz_id)
          .subscribe({
            next: (response: any) => {
              this.questionList = response.result;
              console.log(this.questionList[0])
              this.count = 0;
              this.answers = "";
            }
          });
        }
      }
    })
  }

  onQuestionSubmit() {
    if(this.questionForm.valid && this.isNext()) {
      this.next();
      let answer = this.questionForm.value?.answer;
      this.answers += answer + ",";
    }
    
    if(this.questionForm.valid && !this.isNext()) {
      this.answers = this.answers.slice(0, -1);
      console.log("The overall answer is", this.answers, this.quiz_id);
    }
  }

  isNext() {
    return (this.count + 1) != this.questionList.length;
  }

  next() {
    this.count++;
  }

}
