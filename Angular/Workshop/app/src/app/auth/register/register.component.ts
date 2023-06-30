import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { appEmailDomains } from 'src/app/shared/constants';
import { appEmailValidator } from 'src/app/shared/validators';
import { sameValueGroupValidator } from 'src/app/shared/validators/same-value-group-validator';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent {
  form = this.fb.group({
    username: [
      '', [Validators.required, Validators.minLength(5)]
    ],
    email: [
      '', [Validators.required, appEmailValidator(appEmailDomains)]
    ],
    telephone: [
      '', 
    ],
    ext: [
      '',
    ],
    pass: this.fb.group({
      password: [
        '',
        [Validators.required, Validators.minLength(5)]
      ],
      rePassword: [
        
      ]
    }, { validators: [ sameValueGroupValidator('password', 'rePassword' )] }),
  });

  constructor(
    private fb: FormBuilder,
    private authService: AuthService
  ) { }

  registerHandler() {
    if (this.form.invalid) {
      return;
    }

    const { username, email, pass: {password, rePassword} = {}, telephone} = this.form.value;
    this.authService
      .register(username!, email!, password!, rePassword!, telephone || undefined);
  }
}
