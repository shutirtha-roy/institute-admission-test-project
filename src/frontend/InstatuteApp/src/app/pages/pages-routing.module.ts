import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from '../guards/auth.guard';
import { HomeComponent } from '../shared/components/home/home.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full',
  },
  {
    path: '',
    children: [
      {
        path: 'auth',
        loadChildren: () =>
          import('./auth/auth.module').then((m) => m.AuthModule),
      }
    ]
  },
  {
    path: '',
    children: [
      {
        path: 'admin',
        loadChildren: () =>
          import('./admin/admin.module').then((m) => m.AdminModule),
      }
    ]
  },
  {
    path: '',
    children: [
      {
        path: 'student',
        loadChildren: () =>
          import('./student/student.module').then((m) => m.StudentModule),
      }
    ]
  },
  {
    path: '',
    children: [
      {
        path: 'tutor',
        loadChildren: () =>
          import('./tutor/tutor.module').then((m) => m.TutorModule),
      }
    ]
  },
  {
    path: 'home',
    component: HomeComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PagesRoutingModule { }
