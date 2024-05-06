import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-student-list',
  templateUrl: './student-list.component.html',
  styleUrls: ['./student-list.component.css']
})
export class StudentListComponent implements OnInit{
  studentList!: any[];

  constructor(
    private authService: AuthService,
    private cdr: ChangeDetectorRef) { 

  }

  ngOnInit(): void {
    this.authService.getAllStudents()
    .subscribe({
      next: (students) => {
        this.studentList = students.result.student_list;
      },
      error: (response) => {
        console.log(response)
      }
    })
  }

  approveStudent(email: string) {
    this.authService.approveStudent(email)
    .subscribe({
      next: (response) => {
        this.ngOnInit();
        console.log(response)
      },
      error: (response) => {
        console.log(response)
      }
    });
  }
  
}
