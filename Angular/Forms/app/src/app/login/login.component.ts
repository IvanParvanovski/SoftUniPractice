import { Component, OnInit, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  @ViewChild('loginForm') loginForm!: NgForm;
  
  constructor() { }

  ngOnInit(): void {
  }

  handleFormSubmit(form: NgForm): void {
    if (form.invalid) { return; }
   
    const value: { email: string, password: string } = form.value;
    form.setValue({ email:'', password: ''});

    console.log(value);
    
  }
}
