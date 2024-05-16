import { Component, OnInit } from '@angular/core';
import { CourseService } from 'src/app/services/course.service';

@Component({
  selector: 'app-course',
  templateUrl: './course.component.html',
  styleUrls: ['./course.component.css']
})
export class CourseComponent implements OnInit{
  courseList: any[] = [];

  constructor(
    private courseService: CourseService) { 

  }

  ngOnInit(): void {
    this.courseService.getAllCourses()
    .subscribe({
      next: (courseResponse: any) => {
        this.courseList = courseResponse.result;
      },
      error: (response) => {
        console.log(response)
      }
    })
  }

  deleteCourses(course_code: string) {
    this.courseService.deleteCourse(course_code)
    .subscribe({
      next: (response) => {
        this.ngOnInit();
        console.log(response)
      },
      error: (response) => {
        console.log(response)
      }
    });
  }
}