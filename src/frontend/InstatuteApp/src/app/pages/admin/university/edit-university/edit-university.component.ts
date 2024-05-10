import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { UniversityService } from 'src/app/services/university.service';

@Component({
  selector: 'app-edit-university',
  templateUrl: './edit-university.component.html',
  styleUrls: ['./edit-university.component.css']
})
export class EditUniversityComponent implements OnInit  {
  university!: any;
  universityForm!: FormGroup;
  submitted: boolean = false;

  constructor(
    private route: ActivatedRoute, 
    private universityService: UniversityService, 
    private router: Router,
    private formBuilder: FormBuilder,
    private toastr: ToastrService) { 

  }

  ngOnInit(): void {
    this.universityForm = this.formBuilder.group({
      title: ['', Validators.required],
      description: ['', Validators.required]
    });

    this.getUniversityDetails();
  }

  getUniversityDetails() {
    this.route.paramMap.subscribe({
      next: (params) => {
        const title = params.get('title');

        if (title) {
          this.universityService.getUniversity(title)
          .subscribe({
            next: (response: any) => {
              //console.log(response);
              this.university = response.result;
            
              this.universityForm.setValue({
                title: this.university.title,
                description: this.university.description,
              });
            }
          });
        }
      }
    })
  }

  onUniversityUpdate() {
    this.submitted = true;

    if(this.universityForm.valid)
      {
        this.universityService.updateUniversity(this.universityForm.value)
        .subscribe({
          next: (response) => {
            this.toastr.success("University updated successfully");
            this.router.navigate(['/admin/universities']);
          }
        }); 
      }
  }
}
