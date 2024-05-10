import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { CourseService } from 'src/app/services/course.service';
import { UniversityService } from 'src/app/services/university.service';
@Component({
  selector: 'app-add-course',
  templateUrl: './add-course.component.html',
  styleUrls: ['./add-course.component.css']
})
export class AddCourseComponent implements OnInit  {
  courseForm!: FormGroup;
  submitted: boolean = false;
  universityList: any[] = [];

  constructor(
    private courseService: CourseService, 
    private universityService: UniversityService,
    private router: Router, 
    private toastr: ToastrService,
    private formBuilder: FormBuilder) { 

  }

  ngOnInit(): void {
    this.courseForm = this.formBuilder.group({
      title: ['', Validators.required],
      course_code: ['', Validators.required],
      university_title: ['default', Validators.required],
      description: ['', Validators.required]
    });

    this.getUniversityList();
  }

  getUniversityList() {
    this.universityService.getAllUniversities()
      .subscribe({
        next: (universityResponse: any) => {
          this.universityList = universityResponse.result;
        },
        error: (response) => {
          console.log(response)
        }
    })
  }

  onCourseSubmit() {
    this.submitted = true;

    if(this.courseForm.valid) {
      let courseDetails = { 'title': this.courseForm.value?.title , 
        'course_code': this.courseForm.value?.course_code,
        'university_title': 'Harvard University',
        'description': this.courseForm.value?.description,
      };
      
      this.courseService.createCourse(courseDetails)
      .subscribe({
        next: (res) => {
          this.toastr.success("Course Added Successfully");
          console.log(res);
          this.courseForm.reset();
          this.router.navigate(['/admin/courses']);
        },
        error: (err) => {
          alert(err?.err.message)
        }
      });
    }
  }
}
