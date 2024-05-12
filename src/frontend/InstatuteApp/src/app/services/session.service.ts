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

  createUniversity(sessionObj: any) {
    return this.http.post(`${this.baseUrl}sessionCreate`, sessionObj);
  }

  getAllSessionsByID(sessionId: string) {
    return this.http.get(`${this.baseUrl}getsession/${sessionId}`);
  }

  getAllSessions(email: string) {
    return this.http.get(`${this.baseUrl}getallsessionbytutor/${email}`);
  }

  getAllSessionsForAllStudents() {
     return this.http.get(`${this.baseUrl}getallsession`);
  }

  requestToEnrollStudent(session_id: string, studentEmailObject: any) {
    return this.http.patch(`${this.baseUrl}addstudent/${session_id}`, studentEmailObject)
  }
}
