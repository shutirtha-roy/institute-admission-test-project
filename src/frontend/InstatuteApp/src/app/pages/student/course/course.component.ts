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
    const studentEmailObject = { "student_email": email };

    this.sessionService.requestToEnrollStudent(session_id, studentEmailObject)
      .subscribe({
        next: (response: any) => {
          console.log(response.result);
          this.ngOnInit();
        },
        error: (response) => {
          console.log(response)
        }
    });
  }

  
  getStudentStatus(session: any) {
    const email: string = this.authService.getEmail() ?? "";
    const unapproved_students: any[] = session.unapproved_student_list;

    if (session.approved_student_list.length != 0) {
      const emailExists = unapproved_students.some(student => student.email == email);

      if (emailExists) {
        return "approved"
      }
    }

    if (session.unapproved_student_list.length != 0) {
      const emailExists = unapproved_students.some(student => student.email == email);

      if (emailExists) {
        return "unapproved"
      }
    }

    return "unenrolled";
  }
}
