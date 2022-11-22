import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListComponent } from './list/list.component';

export class Test {

}


@NgModule({
  declarations: [
    ListComponent
  ],
  imports: [
    CommonModule
  ],
  providers: [
    Test // {provide: Test}
  ],
  exports: [
    ListComponent,
  ]
})
export class UserModule { }
