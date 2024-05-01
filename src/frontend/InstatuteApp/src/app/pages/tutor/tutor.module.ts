import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { TutorRoutingModule } from './tutor-routing.module';
import { TutorComponent } from './tutor.component';
import { DashboardComponent } from './dashboard/dashboard.component';


@NgModule({
  declarations: [
    DashboardComponent
  ],
  imports: [
    CommonModule,
    TutorRoutingModule
  ]
})
export class TutorModule { }
