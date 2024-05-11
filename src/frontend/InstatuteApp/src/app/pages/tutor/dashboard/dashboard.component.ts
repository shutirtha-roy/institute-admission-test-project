import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { UserStoreService } from 'src/app/services/user-store.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit  {
  
  constructor(
    private fb: FormBuilder,  
    private router: Router, 
    private userStore: UserStoreService,
    private toaster: ToastrService) { 

  }

  ngOnInit(): void {
  }
}
