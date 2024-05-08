import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-edit-tutor',
  templateUrl: './edit-tutor.component.html',
  styleUrls: ['./edit-tutor.component.css']
})
export class EditTutorComponent implements OnInit  {
  tutor!: any;
  tutorForm!: FormGroup;
  submitted: boolean = false;

  constructor(
    private route: ActivatedRoute, 
    private authService: AuthService, 
    private router: Router,
    private formBuilder: FormBuilder,
    private toastr: ToastrService) { 

  }

  ngOnInit(): void {
    this.tutorForm = this.formBuilder.group({
      name: ['', Validators.required],
      email: ['', Validators.required],
    });

    this.getTutorDetails();
  }

  getTutorDetails() {
    this.route.paramMap.subscribe({
      next: (params) => {
        const email = params.get('email');

        if (email) {
          this.authService.getTutor(email)
          .subscribe({
            next: (response: any) => {
              console.log(response);
              this.tutor = response.result;
            
              this.tutorForm.setValue({
                name: this.tutor.name,
                email: this.tutor.email,
              });
            }
          });
        }
      }
    })
  }

  onTutorUpdate() {
    this.submitted = true;

    if(this.tutorForm.valid)
      {
        this.authService.updateTutor(this.tutorForm.value)
        .subscribe({
          next: (response) => {
            this.toastr.success("Tutor updated successfully");
            this.router.navigate(['/admin/tutors']);
          }
        }); 
      }
  }
}
