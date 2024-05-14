import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { StudentRoutingModule } from './student-routing.module';
import { StudentComponent } from './student.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CourseComponent } from './course/course.component';
import { QuizComponent } from './quiz/quiz.component';
import { MyCoursesComponent } from './course/my-courses/my-courses.component';
import { QuizListComponent } from './quiz/quiz-list/quiz-list.component';
import { QuizAnswerComponent } from './quiz/quiz-answer/quiz-answer.component';
import { ReactiveFormsModule } from '@angular/forms';
import { PerformanceComponent } from './performance/performance.component';


@NgModule({
  declarations: [
    DashboardComponent,
    CourseComponent,
    QuizComponent,
    MyCoursesComponent,
    QuizListComponent,
    QuizAnswerComponent,
    PerformanceComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    StudentRoutingModule
  ]
})
export class StudentModule { }
