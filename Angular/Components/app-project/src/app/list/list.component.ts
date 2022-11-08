import { Component, OnInit } from '@angular/core';
import { ICustomEvent } from '../list-item/list-item.component';


@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})

export class ListComponent {
  users = [
    {
      firstName: 'Ivan',
      lastName: 'Ivanov'
    },
    {
      firstName: 'Petar',
      lastName: 'Petrov'
    }
  ];

  showLastName = false;

  constructor() { }

  handleClickEvent() {
    this.showLastName = !this.showLastName;
  }

  customEventHandler($event: ICustomEvent) {
    console.log($event);
  }
}
