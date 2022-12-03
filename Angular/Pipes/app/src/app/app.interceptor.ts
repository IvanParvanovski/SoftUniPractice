import { Injectable, Provider } from "@angular/core";
import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest, HttpResponse, HTTP_INTERCEPTORS } from "@angular/common/http";
import { mergeMap, Observable, tap } from "rxjs";
import { environment } from "src/environments/environment";

const apiURL = environment.apiURL;

@Injectable(
)
export class AppInterceptor implements HttpInterceptor {
    intercept(
        req: HttpRequest<any>, 
        next: HttpHandler): Observable<HttpEvent<any>> {
        
        let request = req;
        if (request.url.startsWith('/api')) {
            request = req.clone({
                url: req.url.replace('/api', apiURL)
            });
        }

        return next.handle(req).pipe(
            tap((req) => {
                if (req instanceof HttpResponse) {
                    console.log(req.body);
                }
            })
        )
    }
}

export const appInterceptorProvider: Provider = {
    provide: HTTP_INTERCEPTORS,
    useClass: AppInterceptor,
    multi: true
}