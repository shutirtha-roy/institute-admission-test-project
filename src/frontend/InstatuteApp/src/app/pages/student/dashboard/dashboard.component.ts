import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { DashboardService } from 'src/app/services/dashboard.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  dashboardImage!: string;

  constructor(
    private authService: AuthService,
    private dashboardService: DashboardService) { 

  }

  ngOnInit(): void {
    this.getStudentCourseDashboard();
  }

  getStudentCourseDashboard() {
    let email: string | null = this.authService.getEmail();
    
    this.dashboardService.getStudentCourseDashboard(email ?? "")
    .subscribe({
      next: (response: any) => {
        this.dashboardImage = response.result;
      },
      error: (response) => {
        console.log(response)
      }
    })
  }
}
