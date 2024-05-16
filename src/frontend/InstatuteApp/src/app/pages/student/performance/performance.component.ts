import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { QuizAnswerService } from 'src/app/services/quizAnswer.service';
import { SessionService } from 'src/app/services/session.service';

@Component({
  selector: 'app-performance',
  templateUrl: './performance.component.html',
  styleUrls: ['./performance.component.css']
})
export class PerformanceComponent implements OnInit {
  studentPerformanceList!: any[];

  constructor(
    private authService: AuthService,
    private quizAnswerService: QuizAnswerService) { 

  }

  ngOnInit(): void {
    this.getAllStudentPerformance();
  }

  getAllStudentPerformance() {
    const email: string = this.authService.getEmail() ?? "";

    this.quizAnswerService.getQuizAnswerByStudentEmail(email)
      .subscribe({
        next: (response: any) => {
          this.studentPerformanceList = response.result
          const courseCodesToFilter: string[] = Array.from(new Set(this.studentPerformanceList.map(result => result.course.course_code)));
          const filteredResultsByCourse: { [courseCode: string]: any[] } = {};

          courseCodesToFilter.forEach(courseCode => {
              const filteredResultsForCourse: any[] = this.studentPerformanceList.filter(result => result.course.course_code === courseCode);
              filteredResultsByCourse[courseCode] = filteredResultsForCourse;
          });

          console.log(filteredResultsByCourse);
        },
        error: (response) => {
          console.log(response)
        }
    });
  }
}
