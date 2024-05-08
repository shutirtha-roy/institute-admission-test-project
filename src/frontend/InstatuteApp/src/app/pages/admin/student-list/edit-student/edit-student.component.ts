import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-edit-student',
  templateUrl: './edit-student.component.html',
  styleUrls: ['./edit-student.component.css']
})
export class EditStudentComponent implements OnInit {
  student!: any;
  studentForm!: FormGroup;
  submitted: boolean = false;

  constructor(
    private route: ActivatedRoute, 
    private authService: AuthService, 
    private router: Router,
    private formBuilder: FormBuilder,
    private toastr: ToastrService) { 

  }

  ngOnInit(): void {
    this.studentForm = this.formBuilder.group({
      name: ['', Validators.required],
      email: ['', Validators.required],
    });

    this.getStudentDetails();
  }

  getStudentDetails() {
    this.route.paramMap.subscribe({
      next: (params) => {
        const email = params.get('email');

        if (email) {
          this.authService.getStudent(email)
          .subscribe({
            next: (response: any) => {
              console.log(response);
              this.student = response.result;
            
              this.studentForm.setValue({
                name: this.student.name,
                email: this.student.email,
              });
            }
          });
        }
      }
    })
  }

  onStudentUpdate() {
    this.submitted = true;

    if(this.studentForm.valid)
    {
      
    }
  }
}
