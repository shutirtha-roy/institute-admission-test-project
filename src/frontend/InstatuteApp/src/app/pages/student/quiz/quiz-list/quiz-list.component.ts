import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';
import { QuizService } from 'src/app/services/quiz.service';
import { QuizAnswerService } from 'src/app/services/quizAnswer.service';
import { SessionService } from 'src/app/services/session.service';

@Component({
  selector: 'app-quiz-list',
  templateUrl: './quiz-list.component.html',
  styleUrls: ['./quiz-list.component.css']
})
export class QuizListComponent implements OnInit  {
  quizList!: any[];
  courseCode: string | null = "";
  courseQuizList!: any[];
  givenQuizList!: any[];

  constructor(
    private authService: AuthService,
    private sessionService: SessionService,
    private quizService: QuizService,
    private quizAnswerService: QuizAnswerService,
    private route: ActivatedRoute,
    private router: Router,
    private formBuilder: FormBuilder,
    private toastr: ToastrService) { 

  }

  ngOnInit(): void {
    //this.getAllQuizesByCourseCode();
    this.getAllQuestionsByCourseCodeForStudent();
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

  getAllQuestionsByCourseCodeForStudent() {
    this.route.paramMap.subscribe({
      next: (params) => {
        const email: string = this.authService.getEmail() ?? "";
        this.courseCode = params.get('course_code');

        if (this.courseCode) {
          this.quizAnswerService.getCourseQuizByStudentEmail(this.courseCode, email) 
          .subscribe({
            next: (response: any) => {
              this.courseQuizList = response.result.course_quizes;
              this.givenQuizList = response.result.given_quizes;

              console.log("COURSE LIST", this.courseQuizList);
              console.log("GIVEN QUIZ LIST", this.givenQuizList);
              this.quizList = [];
              
              this.courseQuizList.forEach((courseQuiz) => {
                this.givenQuizList.forEach((givenQuiz) => {
                  if (courseQuiz.quiz_id == givenQuiz.quiz_id) {
                    this.quizList.push({
                      quiz_id: courseQuiz.quiz_id,
                      description: courseQuiz.description,
                      status: "Attempted",
                      course_title: courseQuiz.course.title + " (" + courseQuiz.course.course_code + ")",
                      university_title: courseQuiz.course.university_title
                    });
                  }
                });
              });

              this.courseQuizList.forEach((courseQuiz) => {
                let courseObj = this.quizList.some(quiz => quiz.quiz_id == courseQuiz.quiz_id);

                if(!courseObj) {
                  this.quizList.push({
                    quiz_id: courseQuiz.quiz_id,
                    description: courseQuiz.description,
                    status: "Pending",
                    course_title: courseQuiz.course.title + " (" + courseQuiz.course.course_code + ")",
                    university_title: courseQuiz.course.university_title
                  });
                }
              });

              this.givenQuizList.forEach((givenQuiz) => {
                let courseObj = this.quizList.some(quiz => quiz.quiz_id == givenQuiz.quiz_id);

                if(!courseObj) {
                  this.quizList.push({
                    quiz_id: givenQuiz.quiz_id,
                    description: givenQuiz.description,
                    status: "Attempted",
                    course_title: givenQuiz.course.title + " (" + givenQuiz.course.course_code + ")",
                    university_title: givenQuiz.course.university_title
                  });
                }
              });
            }
          });
        }
      }
    })
  }

}
