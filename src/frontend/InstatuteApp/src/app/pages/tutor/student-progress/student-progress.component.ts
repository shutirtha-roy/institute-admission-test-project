import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';
import { QuizService } from 'src/app/services/quiz.service';
import { QuizAnswerService } from 'src/app/services/quizAnswer.service';
import { SessionService } from 'src/app/services/session.service';

@Component({
  selector: 'app-student-progress',
  templateUrl: './student-progress.component.html',
  styleUrls: ['./student-progress.component.css']
})
export class StudentProgressComponent implements OnInit  {
  studentsresultList: any[] = [];
  quizId!: string | null;

  constructor(
    private route: ActivatedRoute, 
    private authService: AuthService,
    private sessionService: SessionService, 
    private quizService: QuizService,
    private quizAnswerService: QuizAnswerService,
    private router: Router,
    private formBuilder: FormBuilder,
    private toastr: ToastrService,
  ) { 

  }

  ngOnInit(): void {
    this.getAllStudentReport();
  }

  getAllStudentReport() {
    this.route.paramMap.subscribe({
      next: (params) => {
        this.quizId = params.get('quiz_id');

        if (this.quizId) {
          this.quizAnswerService.getQuizAnswerById(this.quizId)
          .subscribe({
            next: (response: any) => {
              this.studentsresultList = response.result;
              console.log(this.studentsresultList);
            }
          });
        }
      }
    })
  }
}
