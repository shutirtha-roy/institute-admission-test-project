import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-add-tutor',
  templateUrl: './add-tutor.component.html',
  styleUrls: ['./add-tutor.component.css']
})
export class AddTutorComponent implements OnInit {
  tutorForm!: FormGroup;
  submitted: boolean = false;

  constructor(
    private authService: AuthService, 
    private router: Router, 
    private toastr: ToastrService,
    private formBuilder: FormBuilder) { 

  }

  ngOnInit(): void {
    this.tutorForm = this.formBuilder.group({
      name: ['', Validators.required],
      email: ['', Validators.required],
      password: ['', [Validators.required]]
    });
  }

  onTutorSubmit() {
    this.submitted = true;

    if(this.tutorForm.valid) {
      let signUpDetails = { 'name': this.tutorForm.value?.name , 
        'email': this.tutorForm.value?.email,  
        'password': this.tutorForm.value?.password 
      };
      
      this.authService.createTutor(signUpDetails)
      .subscribe({
        next: (res) => {
          this.toastr.success("Tutor Added Successfully");
          console.log(res);
          this.tutorForm.reset();
          this.router.navigate(['/admin/tutors']);
        },
        error: (err) => {
          alert(err?.err.message)
        }
      });
    }
  }

}
