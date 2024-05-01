import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  type: string = "password";
  isText: boolean = false;
  eyeIcon: string = "fa-eye-slash";
  signUpForm!: FormGroup;
  submitted: boolean = false;

  constructor(private fb: FormBuilder, private auth: AuthService, private router: Router, private toaster: ToastrService) { }

  ngOnInit(): void {
    this.signUpForm = this.fb.group({
      name: ['', Validators.required],
      username: ['', Validators.required],
      password: ['', Validators.required],
      role: ['user'],
    });
  }

  hideShowPass() {
    this.isText = !this.isText;
    this.isText ? this.eyeIcon = "fa-eye" : this.eyeIcon = "fa-eye";
    this.isText ? this.type = "text" : this.type = "password";
  }

  onSignUp() {
    this.submitted = true;

    if(this.signUpForm.valid) {
      console.log(this.signUpForm.value);
      let signUpDetails = { 'name': this.signUpForm.value?.name , 'email': this.signUpForm.value?.username,  'password': this.signUpForm.value?.password };

      this.auth.signUp(signUpDetails)
      .subscribe({
        next: (res) => {
          this.toaster.success("SignUp Successful, please login now");
          console.log(res);
          this.signUpForm.reset();
          this.router.navigate(['/auth/login']);
        },
        error: (err) => {
          alert(err?.err.message)
        }
      });

    }
  }
}