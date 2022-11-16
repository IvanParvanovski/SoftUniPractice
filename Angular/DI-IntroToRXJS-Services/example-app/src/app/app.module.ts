import { InjectionToken, NgModule, Provider } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { TestComponent } from './test/test.component';

export class MyClass {
  constructor() {
    console.log('Nameless class was constructed');
  }
}

// const myProvider: Provider = {
//   useClass: MyClass,
//   provide: MyClass
// };

export const myCustomToken = new InjectionToken('Test');

const myProvider: Provider = {
  useClass: MyClass,
  provide: myCustomToken,
};

@NgModule({
  declarations: [
    AppComponent,
    TestComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [
    myProvider,
    MyClass
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
