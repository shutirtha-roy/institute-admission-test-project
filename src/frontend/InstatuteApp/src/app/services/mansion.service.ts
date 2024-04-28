import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { IMansionApiResponse, IMansionResult } from 'src/assets/data/IMansionApiResonse';

@Injectable({
  providedIn: 'root'
})
export class MansionService {
  private baseUrl: string = "/api/v1/MansionAPI/";

  constructor(private http: HttpClient, private router: Router) { }

  addMansion(addMansionRequest: IMansionResult): Observable<IMansionResult> {
    addMansionRequest.id = '00000000-0000-0000-0000-000000000000';
    return this.http.post<IMansionResult>(this.baseUrl, addMansionRequest);
  }

  getAllMansions(): Observable<IMansionApiResponse> {
    return this.http.get<IMansionApiResponse>(this.baseUrl);
  }

  getAllMansionsForViewers(): Observable<IMansionApiResponse> {
    return this.http.get<IMansionApiResponse>(this.baseUrl + '/all');
  }

  getMansion(id: string): Observable<IMansionApiResponse> {
    return this.http.get<IMansionApiResponse>(this.baseUrl + '/' + id);
  }

  updateMansion(updateEmployeeRequest: IMansionResult): Observable<IMansionResult> {
    return this.http.put<IMansionResult>(this.baseUrl, updateEmployeeRequest);
  }

  deleteMansion(id: string): Observable<IMansionResult> {
    return this.http.delete<IMansionResult>(this.baseUrl + '/' + id);
  }
}