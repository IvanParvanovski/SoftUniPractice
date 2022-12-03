import { Component, OnInit } from '@angular/core';
import { UserService } from './user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  title = 'app';

  obj = {
    scores: [1, 2, 3, 4, 5, 6, 9]
  };

  private scores: number[] = [];
  private result = 0;

  constructor(private userService: UserService) {

  }

  calcScores(obj: { scores: number[] }) {
    if (this.scores !== obj.scores) {
      this.result = obj.scores.reduce((acc, curr) => acc + curr);
      this.scores = obj.scores;

      return this.result;
    }

    return obj.scores.reduce((acc, curr) => acc + curr);
  }

  addProp() {
    (this.obj as any)['test'] = 500;
  }

  ngOnInit(): void {
    this.userService.getUsers().subscribe({
      next: (users) => console.log(users),
      error: (err) => console.log(err)  
    });
  }
}
