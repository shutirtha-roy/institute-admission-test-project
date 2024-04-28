import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  name: any;

  constructor(private auth: AuthService, private router: Router) {

  }

  isAuthenticated(): boolean {
    // if (this.auth.isLoggedIn()) {
    //   this.setName();
    //   return true;
    // }

    return false;
  }

  setName() {
    // this.name = this.auth.getName();
  }

  logout(): void {
    // this.auth.signOut();
  }
}