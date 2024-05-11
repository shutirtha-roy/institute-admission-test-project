import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { SessionService } from 'src/app/services/session';
import { UserStoreService } from 'src/app/services/user-store.service';

@Component({
  selector: 'app-session',
  templateUrl: './session.component.html',
  styleUrls: ['./session.component.css']
})
export class SessionComponent implements OnInit {
  sessionList!: any[];

  constructor(
    private authService: AuthService,
    private userStoreService: UserStoreService,
    private sessionService: SessionService) { 

  }

  ngOnInit(): void {
    this.getAllSessions();
  }

  getAllSessions() {
    this.userStoreService.getEmailForStore()
    .subscribe(email => {
      this.sessionService.getAllSessions(email)
        .subscribe({
          next: (response: any) => {
            this.sessionList = response.result;
          },
          error: (response) => {
            console.log(response)
          }
        })
    })
  }
}
