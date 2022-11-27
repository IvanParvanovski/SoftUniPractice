import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormBuilder, ValidatorFn, Validators } from '@angular/forms';

const myValidator: ValidatorFn = (control: AbstractControl) => {
  return control.value.length > 10 ? { myValidator: true }: null
}

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  registerForm = this.fb.group({
    email: ['', [Validators.required, Validators.email, myValidator]],
    password: ['', [Validators.required, Validators.maxLength(8)]]
  })

  constructor(
    private fb: FormBuilder
  ) { }

  ngOnInit(): void {
  }

  handleFormSubmit() {

  }

}
