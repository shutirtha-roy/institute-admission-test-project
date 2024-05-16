import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { SessionService } from 'src/app/services/session.service';
import { UserStoreService } from 'src/app/services/user-store.service';

@Component({
  selector: 'app-session',
  templateUrl: './session.component.html',
  styleUrls: ['./session.component.css']
})
export class SessionComponent implements OnInit {
  sessionList!: any[];
  isDetailsVisible: boolean[] = [];

  constructor(
    private authService: AuthService,
    private userStoreService: UserStoreService,
    private sessionService: SessionService) { 

  }

  ngOnInit(): void {
    this.getAllSessions();
    this.initializeVisibilityArray();
  }

  initializeVisibilityArray(): void {
    this.isDetailsVisible = new Array(this.sessionList.length).fill(false);
  }

  getAllSessions() {
    const email: string = this.authService.getEmail() ?? "";

    this.sessionService.getAllSessions(email)
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

  toggleDetails(index: number): void {
    this.isDetailsVisible[index] = !this.isDetailsVisible[index];
  }
}

