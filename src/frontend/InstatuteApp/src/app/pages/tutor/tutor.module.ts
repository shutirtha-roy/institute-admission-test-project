import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { TutorRoutingModule } from './tutor-routing.module';
import { TutorComponent } from './tutor.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SessionComponent } from './session/session.component';


@NgModule({
  declarations: [
    DashboardComponent,
    SessionComponent
  ],
  imports: [
    CommonModule,
    TutorRoutingModule
  ]
})
export class TutorModule { }
