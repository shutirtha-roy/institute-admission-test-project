import { Component, OnInit } from '@angular/core';
import { DashboardService } from 'src/app/services/dashboard.service';
import { UniversityService } from 'src/app/services/university.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  alluniversityDashboardImage!: string;

  constructor(
    private dashboardService: DashboardService) { 

  }

  ngOnInit(): void {
    this.getAllUniversityDashboard();
  }

  getAllUniversityDashboard() {
    this.dashboardService.getAllUniversityDashboard()
    .subscribe({
      next: (universityResponse: any) => {
        this.alluniversityDashboardImage = universityResponse.result;
      },
      error: (response) => {
        console.log(response)
      }
    })
  }

}
