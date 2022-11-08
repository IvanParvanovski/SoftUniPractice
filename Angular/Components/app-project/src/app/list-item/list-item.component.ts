import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';

export interface ICustomEvent {
  test: number
}

@Component({
  selector: 'app-list-item',
  templateUrl: './list-item.component.html',
  styleUrls: ['./list-item.component.scss']
})

export class ListItemComponent implements OnInit {
  @Input() userItem!: {
    firstName: string, 
    lastName: string
  }
  @Input() showLastNameValue!: boolean;
  @Output() customEvent = new EventEmitter<ICustomEvent>();

  constructor() { }

  ngOnInit(): void {
    console.log(this.userItem);
    
  }

  selectClickHandler() {
    this.customEvent.emit({ test: 123 });
  }
}
