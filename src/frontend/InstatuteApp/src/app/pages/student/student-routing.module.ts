import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { CourseComponent } from './course/course.component';
import { QuizComponent } from './quiz/quiz.component';
import { MyCoursesComponent } from './course/my-courses/my-courses.component';
import { AddQuestionsComponent } from '../tutor/quiz/add-questions/add-questions.component';
import { RemoveQuestionsComponent } from '../tutor/quiz/remove-questions/remove-questions.component';
import { RemoveQuizComponent } from '../tutor/quiz/remove-quiz/remove-quiz.component';

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
  
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class StudentRoutingModule { }
