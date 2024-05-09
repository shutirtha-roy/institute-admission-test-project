import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { UniversityService } from 'src/app/services/university.service';

@Component({
  selector: 'app-add-university',
  templateUrl: './add-university.component.html',
  styleUrls: ['./add-university.component.css']
})
export class AddUniversityComponent implements OnInit {
  universityForm!: FormGroup;
  submitted: boolean = false;

  constructor(
    private universityService: UniversityService, 
    private router: Router, 
    private toastr: ToastrService,
    private formBuilder: FormBuilder) { 

  }

  ngOnInit(): void {
    this.universityForm = this.formBuilder.group({
      title: ['', Validators.required],
      description: ['', Validators.required]
    });
  }

  onUniversitySubmit() {
    this.submitted = true;

    if(this.universityForm.valid) {
      let universityDetails = { 'title': this.universityForm.value?.title , 
        'description': this.universityForm.value?.description,
      };
      
      this.universityService.createUniversity(universityDetails)
      .subscribe({
        next: (res) => {
          this.toastr.success("University Added Successfully");
          console.log(res);
          this.universityForm.reset();
          this.router.navigate(['/admin/universities']);
        },
        error: (err) => {
          alert(err?.err.message)
        }
      });
    }
  }
}
