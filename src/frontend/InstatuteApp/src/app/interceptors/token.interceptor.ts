import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpErrorResponse
} from '@angular/common/http';
import { catchError, Observable, throwError } from 'rxjs';
import { AuthService } from '../services/auth.service';
import { Router } from '@angular/router';

@Injectable()
export class TokenInterceptor implements HttpInterceptor {

  constructor(private auth: AuthService, private router: Router) {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    const myToken = this.auth.getToken();

    if(myToken) {
      request = request.clone({
        setHeaders: {Authorization: `Bearer ${myToken}`} //Bearer "myToken"
      })
    }

    return next.handle(request).pipe(
      catchError((err: any) => {
        if (err instanceof HttpErrorResponse) {
          if (err.status == 401) {
            //alert("Token is expired, Please login again");
            this.router.navigate(['auth/login']);
          }
        }
        return throwError(() => new Error("Some other error occured"));
      })
    );
  }
}