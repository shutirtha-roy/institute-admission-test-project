import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-add-student',
  templateUrl: './add-student.component.html',
  styleUrls: ['./add-student.component.css']
})
export class AddStudentComponent implements OnInit {
  studentForm!: FormGroup;
  submitted: boolean = false;

  constructor(
    private authService: AuthService, 
    private router: Router, 
    private toastr: ToastrService,
    private formBuilder: FormBuilder) { 

  }

  ngOnInit(): void {
    this.studentForm = this.formBuilder.group({
      name: ['', Validators.required],
      email: ['', Validators.required],
      password: ['', [Validators.required]]
    });
  }

  onStudentSubmit() {
    this.submitted = true;

    if(this.studentForm.valid) {
      let signUpDetails = { 'name': this.studentForm.value?.name , 
        'email': this.studentForm.value?.email,  
        'password': this.studentForm.value?.password 
      };
      
      this.authService.signUp(signUpDetails)
      .subscribe({
        next: (res) => {
          this.toastr.success("Student Added Successfully, please approve now");
          console.log(res);
          this.studentForm.reset();
          this.router.navigate(['/admin/students']);
        },
        error: (err) => {
          alert(err?.err.message)
        }
      });
    }
  }
}
