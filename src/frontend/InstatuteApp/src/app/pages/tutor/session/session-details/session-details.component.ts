import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';
import { SessionService } from 'src/app/services/session.service';

@Component({
  selector: 'app-session-details',
  templateUrl: './session-details.component.html',
  styleUrls: ['./session-details.component.css']
})
export class SessionDetailsComponent implements OnInit  {
  session!: any;
  approved_student_list: any[] = [];
  unapproved_student_list: any[] = [];
  submitted: boolean = false;

  constructor(
    private route: ActivatedRoute, 
    private authService: AuthService,
    private sessionService: SessionService, 
    private router: Router,
    private formBuilder: FormBuilder,
    private toastr: ToastrService) { 

  }

  ngOnInit(): void {
    this.getSessionDetails();
  }

  getSessionDetails() {
    this.route.paramMap.subscribe({
      next: (params) => {
        const sessionId = params.get('session_id');

        if (sessionId) {
          this.sessionService.getAllSessionsByID(sessionId)
          .subscribe({
            next: (response: any) => {
              console.log(response);
              this.session = response.result;
              this.approved_student_list = this.session.approved_student_list;
              this.unapproved_student_list = this.session.unapproved_student_list;
              console.log(this.session);
            }
          });
        }
      }
    })
  }

  approveStudent(student_email: string) {
    const session_id = this.session.session_id;
    const studentEmailObj = { "student_email": student_email };

    this.sessionService.approveStudent(session_id, studentEmailObj)
    .subscribe({
      next: (response: any) => {
        this.ngOnInit();
      }
    });

    console.log(session_id, student_email);
  }
}
