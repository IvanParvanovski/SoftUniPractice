// import { enableProdMode } from '@angular/core';
// import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { map, Observable } from "rxjs";

// import { AppModule } from './app/app.module';
// import { environment } from './environments/environment';

// if (environment.production) {
//   enableProdMode();
// }

// platformBrowserDynamic().bootstrapModule(AppModule)
//   .catch(err => console.error(err));

function interval(delay: number, count: number | null = null) {
	let counter = 0;

	return new Observable(observer => {
		const id = setInterval(() => {
			if (count === counter) {
				observer.complete();
				return;
			}

			observer.next(counter++)
		}, delay);

		return () => {
			clearInterval(id)
		}
	})
}

const sub = interval(1000, 5).subscribe({
	next: (value) => console.log(value),
	error: (error) => console.error(error),
	complete: () => {
		console.log('Observable completed');
	}
});


const s$ = new Observable((observer) => {
	observer.next(100);
	observer.next(200);
	observer.next(300);

	observer.error(new Error('BAD ERROR!'));
});

s$.pipe(
	map((a: any) => a + 1)
).subscribe({
	next: (value) => console.log(value),
	error: (error) => console.error(error)
});