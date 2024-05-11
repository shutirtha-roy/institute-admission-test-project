import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';
import { CourseService } from 'src/app/services/course.service';
import { SessionService } from 'src/app/services/session.service';
import { v4 as uuidv4 } from 'uuid';

@Component({
  selector: 'app-add-session',
  templateUrl: './add-session.component.html',
  styleUrls: ['./add-session.component.css']
})
export class AddSessionComponent implements OnInit  {
  sessionForm!: FormGroup;
  submitted: boolean = false;
  courseList: any[] = [];
  sessionList: any[] = [];

  constructor(
    private sessionService: SessionService,
    private courseService: CourseService,
    private authService: AuthService,
    private router: Router, 
    private toastr: ToastrService,
    private formBuilder: FormBuilder) { 
      
  }

  ngOnInit(): void {
    this.sessionForm = this.formBuilder.group({
      host_email: ['', Validators.required],
      course_code: ['', Validators.required],
      schedule: ['', Validators.required],
      description: ['', Validators.required],
      student_number: [0, Validators.required]
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

  onSessionSubmit() {
    this.submitted = true;

    if(this.sessionForm.valid) {
      const guidId: string = uuidv4();

      let sessionDetails = { 'session_id': guidId, 
        'host_email': this.sessionForm.value?.host_email,
        'course_code': this.sessionForm.value?.course_code,
        'schedule': this.sessionForm.value?.schedule,
        'description': this.sessionForm.value?.description,
        'student_number': this.sessionForm.value?.student_number
      };

      this.sessionService.createUniversity(sessionDetails)
      .subscribe({
            next: (res) => {
              this.toastr.success("Session Added Successfully");
              console.log(res);
              this.sessionForm.reset();
              this.router.navigate(['/tutor/sessions']);
            },
            error: (err) => {
              alert(err?.err.message)
            }
          });
    }
  }
}
