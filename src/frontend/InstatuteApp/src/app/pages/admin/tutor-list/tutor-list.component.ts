import { ChangeDetectorRef, Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-tutor-list',
  templateUrl: './tutor-list.component.html',
  styleUrls: ['./tutor-list.component.css']
})
export class TutorListComponent {
  tutorList!: any[];

  constructor(
    private authService: AuthService,
    private cdr: ChangeDetectorRef) { 

  }

  ngOnInit(): void {
    this.authService.getAllStudents()
    .subscribe({
      next: (students) => {
        this.tutorList = students.result.student_list;
      },
      error: (response) => {
        console.log(response)
      }
    })
  }

  deleteTutors(email: string) {
    this.authService.deleteStudent(email)
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
