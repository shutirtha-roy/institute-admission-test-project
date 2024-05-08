import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { StudentListComponent } from './student-list/student-list.component';
import { TutorListComponent } from './tutor-list/tutor-list.component';
import { AddStudentComponent } from './student-list/add-student/add-student.component';
import { EditStudentComponent } from './student-list/edit-student/edit-student.component';

const routes: Routes = [
  {
    path: 'dashboard',
    component: DashboardComponent
  },
  {
    path: 'students',
    component: StudentListComponent
  },
  {
    path: 'tutors',
    component: TutorListComponent
  },
  {
    path: 'students/add-student',
    component: AddStudentComponent
  },
  {
    path: 'students/edit/:email',
    component: EditStudentComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdminRoutingModule { }
