import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class SessionService {
  private baseUrl: string = "/api/v1/session/";

  constructor(
    private http: HttpClient, 
    private router: Router) { 
  }

  getAllSessions(email: string) {
    return this.http.get(`${this.baseUrl}getallsessionbytutor/${email}`);
  }

  // getUniversity(title: string) {
  //   return this.http.get(`${this.baseUrl}/getuniversity/${title}`);
  // }

  // getAllUniversities() {
  //   return this.http.get(`${this.baseUrl}getalluniversity`);
  // }

  // createUniversity(universityObj: any) {
  //   return this.http.post(`${this.baseUrl}universityCreate`, universityObj);
  // }

  // updateUniversity(universityObj: any) {
  //   return this.http.patch(`${this.baseUrl}updateuniversity/${universityObj.title}`, universityObj);
  // }

  // deleteUniversity(title: string) {
  //   return this.http.delete(`${this.baseUrl}${title}`);
  // }
}
