import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {
  private baseUrl: string = "/api/v1/dashboard/";

  constructor(
    private http: HttpClient, 
    private router: Router) { 
  }

  getAllUniversityDashboard() {
    return this.http.get(`${this.baseUrl}getUniversityDashboard`);
  }

  getUniversityCourseDashboard(university_title: string) {
    return this.http.get(`${this.baseUrl}getUniversityCourseDashboard/${university_title}`);
  }
}
