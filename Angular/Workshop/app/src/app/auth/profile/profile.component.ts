import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { appEmailDomains } from 'src/app/shared/constants';
import { appEmailValidator } from 'src/app/shared/validators';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})

export class ProfileComponent  {
  form = this.fb.group({
    username: [
      '', [Validators.required, Validators.minLength(5)]
    ],
    email: [
      '', [Validators.required, appEmailValidator(appEmailDomains)]
    ],
    ext: [
      ''
    ],
    tel: [
      ''
    ]
  })

  showEditMode = false;

  get user() {
    const {username, email, tel: telephone} = this.authService.user!;
    const [ext, ...tel] = telephone.split(' '); 
    return {
      username,
      email,
      tel: tel.join(' '),
      ext
    };
  }

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
  ) { }

  toggleEditMode(): void {
    this.showEditMode = !this.showEditMode;
    
    this.form.setValue(this.user);
  }

  saveProfile(): void {
    if (this.form.invalid) {
      return;
    }

    const {username, email, ext, tel} = this.form.value;
    this.authService.user = {
      username, email, tel: ext + ' ' + tel
    } as any

    this.toggleEditMode();

  }
}
