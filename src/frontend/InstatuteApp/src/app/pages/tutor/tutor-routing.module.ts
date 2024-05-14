import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SessionComponent } from './session/session.component';
import { QuizComponent } from './quiz/quiz.component';
import { AddSessionComponent } from './session/add-session/add-session.component';
import { SessionDetailsComponent } from './session/session-details/session-details.component';
import { AddQuestionsComponent } from './quiz/add-questions/add-questions.component';
import { RemoveQuestionsComponent } from './quiz/remove-questions/remove-questions.component';
import { RemoveQuizComponent } from './quiz/remove-quiz/remove-quiz.component';
import { AddQuizComponent } from './quiz/add-quiz/add-quiz.component';
import { StudentProgressComponent } from './student-progress/student-progress.component';

const routes: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent
  },
  {
    path: 'sessions',
    component: SessionComponent
  },
  {
    path: 'sessions/add-session',
    component: AddSessionComponent
  },
  {
    path: 'sessions/details/:session_id',
    component: SessionDetailsComponent
  },
  {
    path: 'online-quiz',
    component: QuizComponent
  },
  {
    path: 'online-quiz/add-quiz',
    component: AddQuizComponent
  },
  {
    path: 'online-quiz/add-questions/:quiz_id',
    component: AddQuestionsComponent
  },
  {
    path: 'online-quiz/remove-questions/:quiz_id',
    component: RemoveQuestionsComponent
  },
  {
    path: 'online-quiz/remove-quiz/:quiz_id',
    component: RemoveQuizComponent
  },
  {
    path: 'performance',
    component: StudentProgressComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TutorRoutingModule { }
