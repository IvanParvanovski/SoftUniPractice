import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'app-project';

  changeTitleHandler(newTitle: string) {
    this.title = newTitle
  }

}

