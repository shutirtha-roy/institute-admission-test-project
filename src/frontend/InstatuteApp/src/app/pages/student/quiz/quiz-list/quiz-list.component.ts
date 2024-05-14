import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';
import { QuizService } from 'src/app/services/quiz.service';
import { SessionService } from 'src/app/services/session.service';

@Component({
  selector: 'app-quiz-list',
  templateUrl: './quiz-list.component.html',
  styleUrls: ['./quiz-list.component.css']
})
export class QuizListComponent implements OnInit  {
  quizList!: any[];
  courseCode: string | null = "";

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
    this.getAllQuizesByCourseCode();
  }

  getAllQuizesByCourseCode() {
    this.route.paramMap.subscribe({
      next: (params) => {
        this.courseCode = params.get('course_code');

        if (this.courseCode) {
          this.quizService.getAllQuizByCourse(this.courseCode)
          .subscribe({
            next: (response: any) => {
              console.log(response);
              this.quizList = response.result;
            }
          });
        }
      }
    })
  }

}
