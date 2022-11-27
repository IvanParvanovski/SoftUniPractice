import { enableProdMode } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';
import { environment } from './environments/environment';

if (environment.production) {
  enableProdMode();
}

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));

// interface IRender<T> {
//   createTextElement(content: string): T;
// }

// class DOMRendered implements IRender<HTMLElement> {
//   private createElement(elementType: string, content: string): HTMLElement {
//     const el = document.createElement(elementType);
//     el.textContent = content;
    
//     return el;
//   }

//   createTextElement(content: string): HTMLElement {
//     return this.createElement('p', content);
//   }
// }

// class MDRendered implements IRender<any> {
//   createTextElement(content: string) {
//     return '```' + {content} + '```';
//   }
// }

// const domRender = new MDRendered();
// domRender.createTextElement('Hello');