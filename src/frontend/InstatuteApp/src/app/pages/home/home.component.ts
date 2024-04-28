import { Component, OnInit } from '@angular/core';
import { MansionService } from 'src/app/services/mansion.service';
import { IMansionResult } from 'src/assets/data/IMansionApiResonse';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  mansionlist!: IMansionResult[];

  constructor(private mansionService: MansionService) { }

  ngOnInit(): void {
    this.mansionService.getAllMansionsForViewers()
    .subscribe({
      next: (mansions) => {
        this.mansionlist = mansions.result;
        console.log(this.mansionlist);
      },
      error: (response) => {
        console.log(response)
      }
    });
  }
}
