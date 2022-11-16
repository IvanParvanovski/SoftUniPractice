import { ChangeDetectionStrategy, ChangeDetectorRef, Component, Injector, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { AppComponent } from '../app.component';
import { MyClass, myCustomToken } from '../app.module';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush
})

export class TestComponent implements OnInit, OnChanges {
  @Input() users!: { name: string } [];

  constructor(
    private cdRef: ChangeDetectorRef,
    private injector: Injector
  ) { 
    this.cdRef.detach();

    const value = this.injector.get(myCustomToken);
    const appCmp = this.injector.get(AppComponent);

    console.log(value, appCmp);
    
  }

  ngOnInit(): void {
    this.cdRef.detectChanges();
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (this.users.length > 4) {
      this.cdRef.detectChanges();
    }  
    console.log(changes);
  }

}

// const injector = {
//   collection: new Map(),

//   provide(key: any, value: any) {
//     this.collection.set(key, value);
//   },

//   get(key: any, defaultValue?: any): any {
//     const result = this.collection.get(key);
    
//     if (!result) {
//       if (defaultValue) {return defaultValue}
//       throw new Error('Value not found in injector');
//     }

//     return result;
//   }
// };

// type Injector = typeof injector;
// const amount = Symbol('Amount')

// class Wallet {
//   private amount: number;

//   constructor(private injector: Injector){
//     this.amount = injector.get(amount, 0);
//   }
// }

// class Person {
//   private wallet: Wallet;

//   constructor(private injector: Injector) {
//     this.wallet = injector.get(Wallet);
//   }
// }

// injector.provide(Wallet, Wallet);
// injector.provide(amount, 20);


// const w = new Wallet(injector);
// const p = new Person(injector);
