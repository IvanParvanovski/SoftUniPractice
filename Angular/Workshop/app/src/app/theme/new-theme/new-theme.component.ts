import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-new-theme',
  templateUrl: './new-theme.component.html',
  styleUrls: ['./new-theme.component.scss']
})
export class NewThemeComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  newThemeHandler(form: NgForm) {
    if (form.invalid) { return; }
    console.log(form.value);
  }

}
