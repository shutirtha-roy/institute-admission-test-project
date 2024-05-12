import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { SessionService } from 'src/app/services/session.service';

@Component({
  selector: 'app-session',
  templateUrl: './course.component.html',
  styleUrls: ['./course.component.css']
})
export class CourseComponent implements OnInit {
  sessionList!: any[];

  constructor(
    private authService: AuthService,
    private sessionService: SessionService) { 

  }

  ngOnInit(): void {
    this.getAllSessions();
  }

  getAllSessions() {
    const email: string = this.authService.getEmail() ?? "";

    this.sessionService.getAllSessionsForAllStudents()
      .subscribe({
        next: (response: any) => {
          this.sessionList = response.result;
          console.log(response.result);
        },
        error: (response) => {
          console.log(response)
        }
    });
  }

  requestToEnroll(session_id: string) {
    const email: string = this.authService.getEmail() ?? "";

    
  }
}
