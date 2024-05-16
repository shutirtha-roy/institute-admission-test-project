import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { SessionService } from 'src/app/services/session.service';
import { UserStoreService } from 'src/app/services/user-store.service';

@Component({
  selector: 'app-session',
  templateUrl: './session.component.html',
  styleUrls: ['./session.component.css']
})
export class SessionComponent {
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
    this.sessionService.getAllSessionForAdmin()
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
}
