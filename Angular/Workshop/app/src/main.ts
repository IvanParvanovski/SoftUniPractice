import { enableProdMode } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';


import { AppModule } from './app/app.module';
import { environment } from './environments/environment';

if (environment.production) {
  enableProdMode();
}

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));

// const subject$$ = new Subject();
// const obs$ = subject$$.asObservable();

// const observable$ = new Observable(observer => {
//   let counter = 0;

//   const id = setInterval(() => {
//     observer.next(counter++);
//   }, 1000);

//   return () => {
//     clearInterval(id);
//   };
// });

// const subscription1 = observable$.subscribe({
//   next: (value) => console.log('sub1', value),
//   error: (error) => console.error(error),
//   complete: () => console.log('Completed 1')
// });

// observable$.subscribe(subject$$);


// setTimeout(() => {
//   subscription1.unsubscribe();

//   const subscription2 = observable$.subscribe({
//     next: (value) => console.log('sub2', value),
//     complete: () => console.log('Completed 2')
//   });
// }, 2000);
