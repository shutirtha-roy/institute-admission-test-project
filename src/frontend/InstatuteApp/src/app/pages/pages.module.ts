import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { PagesRoutingModule } from './pages-routing.module';
import { AuthComponent } from './auth/auth.component';
import { HomeComponent } from '../shared/components/home/home.component';
import { NgxDatatableModule } from '@swimlane/ngx-datatable';
import { AdminComponent } from './admin/admin.component';
import { StudentComponent } from './student/student.component';
import { TutorComponent } from './tutor/tutor.component';


@NgModule({
  declarations: [
    AuthComponent,
    AdminComponent,
    StudentComponent,
    TutorComponent,
  ],
  imports: [
    CommonModule,
    PagesRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    NgxDatatableModule
  ]
})
export class PagesModule { }
