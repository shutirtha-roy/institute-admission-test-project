import { ChangeDetectorRef, Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-tutor-list',
  templateUrl: './tutor-list.component.html',
  styleUrls: ['./tutor-list.component.css']
})
export class TutorListComponent {
  tutorList: any[] = [];

  constructor(
    private authService: AuthService,
    private cdr: ChangeDetectorRef) { 

  }

  ngOnInit(): void {
    this.authService.getAllTutors()
    .subscribe({
      next: (tutors: any) => {
        console.log(tutors.result);
        this.tutorList = tutors.result;
      },
      error: (response) => {
        console.log(response)
      }
    })
  }

  deleteTutors(email: string) {
    this.authService.deleteTutor(email)
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
