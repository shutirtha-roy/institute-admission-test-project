import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-student-list',
  templateUrl: './student-list.component.html',
  styleUrls: ['./student-list.component.css']
})
export class StudentListComponent implements OnInit{
  
  studentList: any[] = [
    {
      _id: '1',
      password: "",
      role: "student",
      name: "Fahim Shahrear",
      email: "fahim@gmail.com",
      approved: false
    }
  ];

  constructor(
    private auth: AuthService) { 

  }

  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }
  
}
