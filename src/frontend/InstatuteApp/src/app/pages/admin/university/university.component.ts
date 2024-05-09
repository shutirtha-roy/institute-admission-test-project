import { Component, OnInit } from '@angular/core';
import { UniversityService } from 'src/app/services/university.service';

@Component({
  selector: 'app-university',
  templateUrl: './university.component.html',
  styleUrls: ['./university.component.css']
})
export class UniversityComponent  implements OnInit{
  universityList: any[] = [
    {
      "title": "Swinburne University of Technology",
      "description": "Best for IT related courses with high QS ranking.",
      "tutor_list": [
        "Samin", "Kabir"
      ],
      "course_list": [
        "Physics", "Maths"
      ]
    }
  ];

  constructor(
    private universityService: UniversityService) { 

  }

  ngOnInit(): void {
    this.universityService.getAllUniversities()
    .subscribe({
      next: (universityResponse: any) => {
        this.universityList = universityResponse.result;
      },
      error: (response) => {
        console.log(response)
      }
    })
  }

  deleteUniversities(title: string) {
    this.universityService.deleteUniversity(title)
    .subscribe({
      next: (response) => {
        this.ngOnInit();
        console.log(response)
      },
      error: (response) => {
        console.log(response)
      }
    });
  }
}
