import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AdminRoutingModule } from './admin-routing.module';
import { AdminComponent } from './admin.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { StudentListComponent } from './student-list/student-list.component';
import { TutorListComponent } from './tutor-list/tutor-list.component';
import { AddStudentComponent } from './student-list/add-student/add-student.component';
import { ReactiveFormsModule } from '@angular/forms';
import { EditStudentComponent } from './student-list/edit-student/edit-student.component';
import { AddTutorComponent } from './tutor-list/add-tutor/add-tutor.component';
import { EditTutorComponent } from './tutor-list/edit-tutor/edit-tutor.component';
import { UniversityComponent } from './university/university.component';
import { CourseComponent } from './course/course.component';
import { AddUniversityComponent } from './university/add-university/add-university.component';
import { EditUniversityComponent } from './university/edit-university/edit-university.component';
import { AddCourseComponent } from './course/add-course/add-course.component';
import { EditCourseComponent } from './course/edit-course/edit-course.component';
import { AssignTutorComponent } from './course/assign-tutor/assign-tutor.component';
import { SessionComponent } from './session/session.component';


@NgModule({
  declarations: [
    DashboardComponent,
    StudentListComponent,
    TutorListComponent,
    AddStudentComponent,
    EditStudentComponent,
    AddTutorComponent,
    EditTutorComponent,
    UniversityComponent,
    CourseComponent,
    AddUniversityComponent,
    EditUniversityComponent,
    AddCourseComponent,
    EditCourseComponent,
    AssignTutorComponent,
    SessionComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    AdminRoutingModule
  ]
})
export class AdminModule { }
