import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { StudentListComponent } from './student-list/student-list.component';
import { TutorListComponent } from './tutor-list/tutor-list.component';
import { AddStudentComponent } from './student-list/add-student/add-student.component';
import { EditStudentComponent } from './student-list/edit-student/edit-student.component';
import { AddTutorComponent } from './tutor-list/add-tutor/add-tutor.component';
import { EditTutorComponent } from './tutor-list/edit-tutor/edit-tutor.component';
import { UniversityComponent } from './university/university.component';
import { AddUniversityComponent } from './university/add-university/add-university.component';
import { EditUniversityComponent } from './university/edit-university/edit-university.component';
import { CourseComponent } from './course/course.component';
import { AddCourseComponent } from './course/add-course/add-course.component';
import { EditCourseComponent } from './course/edit-course/edit-course.component';

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
    path: 'universities',
    component: UniversityComponent
  },
  {
    path: 'courses',
    component: CourseComponent
  },
  {
    path: 'students/add-student',
    component: AddStudentComponent
  },
  {
    path: 'students/edit/:email',
    component: EditStudentComponent
  },
  {
    path: 'tutors/add-tutor',
    component: AddTutorComponent
  },
  {
    path: 'tutors/edit/:email',
    component: EditTutorComponent
  },
  {
    path: 'universities/add-university',
    component: AddUniversityComponent
  },
  {
    path: 'universities/edit/:title',
    component: EditUniversityComponent
  },
  {
    path: 'courses/add-course',
    component: AddCourseComponent
  },
  {
    path: 'courses/edit/:course-code',
    component: EditCourseComponent
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdminRoutingModule { }
