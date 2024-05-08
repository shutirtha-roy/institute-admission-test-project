import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';
import { UserStoreService } from 'src/app/services/user-store.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  type: string = "password";
  isText: boolean = false;
  eyeIcon: string = "fa-eye-slash";
  loginForm!: FormGroup;
  submitted: boolean = false;
  
  constructor(
    private fb: FormBuilder, 
    private auth: AuthService, 
    private router: Router, 
    private userStore: UserStoreService,
    private toaster: ToastrService) { 

  }

  ngOnInit(): void {
    this.loginForm = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    })
  }

  onLogin() {
    this.submitted = true;

    if(this.loginForm.valid) {
      this.submitted = true;
      let loginDetails = { 'email': this.loginForm.value?.username , 'password': this.loginForm.value?.password };
      this.auth.login(loginDetails)
      .subscribe({
        next: (res) => {
          this.auth.storeToken(res.data.access_token);
          const tokenPayload = this.auth.decodeToken();
          this.userStore.setFullNameForStore(tokenPayload.unique_name);
          this.userStore.setRoleForStore(tokenPayload.role);
          this.auth.storeName(res.data.user.name);
          this.loginForm.reset();
          console.log(res.message);

          if(tokenPayload.role == 'student') {
            this.router.navigate(['/student/dashboard']);
            return;
          }

          if(tokenPayload.role == 'tutor') {
            this.router.navigate(['/tutor/dashboard']);
            return;
          }

          if(tokenPayload.role == 'admin') {
            this.router.navigate(['/admin/dashboard']);
            return;
          }
          
          this.router.navigate(['/']);
        },
        error: (err) => {
          //alert(err?.err.message)
          this.toaster.success("Invalid Email or Password");
        },
        complete: () => {
          this.toaster.success("Login Successful");
        }
      })
    }
  }
}