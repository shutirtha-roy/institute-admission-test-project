import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { TutorRoutingModule } from './tutor-routing.module';
import { TutorComponent } from './tutor.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SessionComponent } from './session/session.component';
import { QuizComponent } from './quiz/quiz.component';
import { AddSessionComponent } from './session/add-session/add-session.component';
import { ReactiveFormsModule } from '@angular/forms';
import { SessionDetailsComponent } from './session/session-details/session-details.component';
import { AddQuestionsComponent } from './quiz/add-questions/add-questions.component';
import { AddQuizComponent } from './quiz/add-quiz/add-quiz.component';
import { RemoveQuestionsComponent } from './quiz/remove-questions/remove-questions.component';
import { RemoveQuizComponent } from './quiz/remove-quiz/remove-quiz.component';


@NgModule({
  declarations: [
    DashboardComponent,
    SessionComponent,
    QuizComponent,
    AddQuestionsComponent,
    AddQuizComponent,
    RemoveQuestionsComponent,
    RemoveQuizComponent,
    AddSessionComponent,
    SessionDetailsComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    TutorRoutingModule
  ]
})
export class TutorModule { }
