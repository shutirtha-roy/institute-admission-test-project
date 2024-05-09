import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class UniversityService {
  private baseUrl: string = "/api/v1/university/";

  constructor(
    private http: HttpClient, 
    private router: Router) { 
  }

  getAllUniversities() {
    return this.http.get(`${this.baseUrl}getalluniversity`);
  }

  createUniversity(universityObj: any) {
    return this.http.post(`${this.baseUrl}/universityCreate`, universityObj);
  }

  deleteUniversity(title: string) {
    return this.http.delete(`${this.baseUrl}${title}`);
  }
}
