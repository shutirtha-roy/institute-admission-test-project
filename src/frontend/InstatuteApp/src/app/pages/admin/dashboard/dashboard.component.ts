import { Component, OnInit } from '@angular/core';
import { DashboardService } from 'src/app/services/dashboard.service';
import { UniversityService } from 'src/app/services/university.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  noOfStudents: number = 0;
  noOfTutors: number = 0;
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
        this.noOfStudents = universityResponse.result.number_of_students;
        this.noOfTutors = universityResponse.result.number_of_tutors;
        this.alluniversityDashboardImage = universityResponse.result.my_base64_jpgData;
      },
      error: (response) => {
        console.log(response)
      }
    })
  }

}
