import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';
import { CourseService } from 'src/app/services/course.service';
import { UniversityService } from 'src/app/services/university.service';

@Component({
  selector: 'app-assign-tutor',
  templateUrl: './assign-tutor.component.html',
  styleUrls: ['./assign-tutor.component.css']
})
export class AssignTutorComponent implements OnInit   {
  assignTutorToCourseForm!: FormGroup;
  submitted: boolean = false;
  tutorList: any[] = [];
  courseList: any[] = [];

  constructor(
    private courseService: CourseService, 
    private router: Router, 
    private toastr: ToastrService,
    private formBuilder: FormBuilder,
    private authService: AuthService) { 

  }

  ngOnInit(): void {
    this.assignTutorToCourseForm = this.formBuilder.group({
      email: ['default', Validators.required],
      course_code: ['default', Validators.required],
    });

    this.getTutorEmailList();
    this.getCourseList();
  }

  getTutorEmailList() {
    this.authService.getAllTutors()
    .subscribe({
      next: (tutors: any) => {
        console.log("TUTORS in ASSIGN TUTORS TO COURSES", tutors.result);
        this.tutorList = tutors.result;
      },
      error: (response) => {
        console.log(response)
      }
    })
  }

  getCourseList() {
    this.courseService.getAllCourses()
    .subscribe({
      next: (courseResponse: any) => {
        console.log("COURSES in ASSIGN TUTORS TO COURSES", courseResponse.result);
        this.courseList = courseResponse.result;
      },
      error: (response) => {
        console.log(response);
      }
    })
  }

  onTutorAssignSubmit() {
    this.submitted = true;

    if(this.assignTutorToCourseForm.valid) {
      let assignTutorsToCourseData = { 'course_code': this.assignTutorToCourseForm.value?.course_code };
      
      this.courseService.assignTutorToCourse(this.assignTutorToCourseForm.value?.email, 
        assignTutorsToCourseData)
      .subscribe({
        next: (res) => {
          this.toastr.success("Tutor Assigned To Courses Successfully");
          console.log(res);
          this.assignTutorToCourseForm.reset();
          this.router.navigate(['/admin/courses']);
        },
        error: (err) => {
          alert(err?.err.message)
        }
      });
    }
  }
}
