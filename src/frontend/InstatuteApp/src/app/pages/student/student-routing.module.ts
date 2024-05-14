import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CourseComponent } from './course/course.component';
import { QuizComponent } from './quiz/quiz.component';
import { MyCoursesComponent } from './course/my-courses/my-courses.component';
import { QuizListComponent } from './quiz/quiz-list/quiz-list.component';
import { QuizAnswerComponent } from './quiz/quiz-answer/quiz-answer.component';
import { PerformanceComponent } from './performance/performance.component';

const routes: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent
  },
  {
    path: 'courses',
    component: CourseComponent
  },
  {
    path: 'online-quiz',
    component: QuizComponent
  },
  {
    path: 'my-courses',
    component: MyCoursesComponent
  },
  {
    path: 'online-quiz/quizes/:course_code',
    component: QuizListComponent
  },
  {
    path: 'online-quiz/mock/:quiz_id',
    component: QuizAnswerComponent
  },
  {
    path: 'performance',
    component: PerformanceComponent
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class StudentRoutingModule { }
