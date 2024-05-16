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
  role: any;

  constructor(private auth: AuthService, 
    private router: Router) {

  }

  isAuthenticated(): boolean {
    if (this.auth.isLoggedIn()) {
      this.setName();
      this.setRole();
      return true;
    }

    return false;
  }

  setName() {
    this.name = this.auth.getName();
  }

  setRole() {
    this.role = this.auth.getRoleFromToken();
  }

  logout(): void {
    this.auth.signOut();
  }

  isActive(route: string): boolean {
    return this.router.url === route;
  }
}