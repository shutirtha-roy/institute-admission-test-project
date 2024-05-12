import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SessionComponent } from './session/session.component';
import { QuizComponent } from './quiz/quiz.component';
import { AddSessionComponent } from './session/add-session/add-session.component';
import { SessionDetailsComponent } from './session/session-details/session-details.component';

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
    path: 'online-quiz',
    component: QuizComponent
  },
  {
    path: 'sessions/add-session',
    component: AddSessionComponent
  },
  {
    path: 'sessions/details/:session_id',
    component: SessionDetailsComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TutorRoutingModule { }
