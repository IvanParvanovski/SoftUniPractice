// import { enableProdMode } from '@angular/core';
// import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { Observable, map, interval } from "rxjs";


// import { AppModule } from './app/app.module';
// import { environment } from './environments/environment';

// if (environment.production) {
//   enableProdMode();
// }

// platformBrowserDynamic().bootstrapModule(AppModule)
//   .catch(err => console.error(err));

function invterval(intervalValue: number = 0) {
  return new Observable<number>(observer => {
    let counter = 0;
    setInterval(() => {
      observer.next(counter++)
    }, intervalValue);
  })
}

const stream$ = interval(1000).pipe(
  map(x => x + 1),
  map(x => x + 1),
  map(x => x + 1),
  map(x => x + 1),
);

setTimeout(() => {
  const sub = stream$.subscribe(console.log)

  setInterval(() => {
    sub.unsubscribe();
  })
}, 3000);
