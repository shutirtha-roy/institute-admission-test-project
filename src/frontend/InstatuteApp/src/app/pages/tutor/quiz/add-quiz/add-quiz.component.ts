import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';
import { CourseService } from 'src/app/services/course.service';
import { QuizService } from 'src/app/services/quiz.service';
import { SessionService } from 'src/app/services/session.service';
import { v4 as uuidv4 } from 'uuid';

@Component({
  selector: 'app-add-quiz',
  templateUrl: './add-quiz.component.html',
  styleUrls: ['./add-quiz.component.css']
})
export class AddQuizComponent implements OnInit   {
  quizForm!: FormGroup;
  submitted: boolean = false;
  courseList: any[] = [];
  sessionList: any[] = [];

  constructor(
    private sessionService: SessionService,
    private courseService: CourseService,
    private authService: AuthService,
    private quizService: QuizService,
    private router: Router, 
    private toastr: ToastrService,
    private formBuilder: FormBuilder) { 
      
  }

  ngOnInit(): void {
    this.quizForm = this.formBuilder.group({
      course_code: ['default', Validators.required],
      description: ['', Validators.required],
    });

    this.getCourseList();
  }

  getCourseList() {
    const email: string = this.authService.getEmail() ?? "";

    this.authService.getTutor(email)
     .subscribe({
        next: (response: any) => {
          const courseCodeList: any[] = response.result.course_list;

          courseCodeList.forEach((courseCode, index) => {
            this.courseService.getCourseByCode(courseCode)
              .subscribe({
                next: (courseResponse: any) => {
                  this.courseList.push(courseResponse.result);
                },
                error: (courseResponse) => {
                  console.log(courseResponse)
                }
              });
          });

        },
        error: (response) => {
          console.log(response)
        }
    })

    console.log("Course List", this.courseList);
  }

  onQuizSubmit() {
    this.submitted = true;
    const email: string = this.authService.getEmail() ?? "";

    if(this.quizForm.valid) {
      const guidId: string = uuidv4();

      let quizDetails = { 'quiz_id': guidId, 
        'tutor_email': email,
        'course_code': this.quizForm.value?.course_code,
        'description': this.quizForm.value?.description,
      };

      this.quizService.createQuiz(quizDetails)
      .subscribe({
            next: (res) => {
              this.toastr.success("Session Added Successfully");
              console.log(res);
              this.quizForm.reset();
              this.router.navigate(['/tutor/online-quiz']);
            },
            error: (err) => {
              alert(err?.err.message)
            }
          });
    }
  }
}
