import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { SessionService } from 'src/app/services/session.service';

@Component({
  selector: 'app-my-courses',
  templateUrl: './my-courses.component.html',
  styleUrls: ['./my-courses.component.css']
})
export class MyCoursesComponent {
  sessionList!: any[];
  approvedStudentList!: any[];

  constructor(
    private authService: AuthService,
    private sessionService: SessionService) { 

  }

  ngOnInit(): void {
    this.getAllApprovedStudentSessions();
  }

  getAllApprovedStudentSessions() {
    this.sessionService.getAllSessionsForAllStudents()
      .subscribe({
        next: (response: any) => {
          this.sessionList = response.result;
          this.approvedStudentList = this.getApprovedStudentList(this.sessionList);
          console.log("APPROVED STUDENT COURSE", this.approvedStudentList);
        },
        error: (response) => {
          console.log(response)
        }
    });
  }

  getApprovedStudentList(sessionList: any[]) {
    let approvedStudentList: any[] = [];
    const email: string = this.authService.getEmail() ?? "";

    sessionList.forEach((session) => {
      let approved_students: any[] = session.approved_student_list;

      if (approved_students.length != 0) {
        const emailExists = approved_students.some(student => student.email == email);
  
        if (emailExists) {
          approvedStudentList.push(session);
        }
      }
    });

    return approvedStudentList;
  }
}
