import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-student-list',
  templateUrl: './student-list.component.html',
  styleUrls: ['./student-list.component.css']
})
export class StudentListComponent implements OnInit{
  studentList!: any[];

  constructor(
    private authService: AuthService) { 

  }

  ngOnInit(): void {
    this.authService.getAllStudents()
    .subscribe({
      next: (students) => {
        this.studentList = students.result.studentt_list;
      },
      error: (response) => {
        console.log(response)
      }
    })
  }
  
}
