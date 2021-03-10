 int player1Score = 0;
  int player2Score = 0;
   boolean swap = true;
    float cubeScore = 0;

 int rectX = 25;
  int rectY = 10;
   int ButtonX = 250;
    int ButtonY = 50;
     int ButtonW = 125;
      int ButtonH = 50;

void setup(){
  size(500,500);

}

void draw(){
  //BasicSettings
 background(35, 8, 59);
  fill(80, 79, 82);
   strokeWeight(10);
    rect(rectX,rectY,150,150);
     fill(80, 79, 82);
      strokeWeight(8);
       rect(ButtonX,ButtonY,125,50);

//Player1Score
 rect(10,410,285,80);
  fill(0);
   textSize(32);
    text("Player1Score:", 20, 460);
     textSize(32);
      text(player1Score, 230, 460); 

//Player2Score
 fill(80,79,82);
  rect(200,315,285,80);
   fill(0);
    textSize(32);
     text("Player2Score:", 210, 365);
      textSize(32);
       text(player2Score, 420,365); 

//ButtonRowText
 fill(0);
  textSize(25);
   text("Row!", 280, 85); 

//CheckScore
 if(player1Score >= 100){
   player2Score = 0;
    fill(80,79,82);
     rect(100,200,315,70);
      fill(0);
    player1Score = 100;
     textSize(45);
      text("Player1 Wins!", 120, 250);
       println("You Win!");  
}

 if(player2Score >= 100){
 player1Score = 0;
  fill(80,79,82);
   rect(100,200,315,75);
    fill(0);
 player2Score = 100;
   textSize(45);
    text("Player2 Wins!", 120, 250);
     println("You Win!"); 
}
 
if(int(cubeScore) == 1){
  fill(135, 0, 255);
 ellipse(100, 85, 25,25);
 }
 
 if(int(cubeScore) == 2){
   fill(135, 0, 255);
 ellipse(150, 35, 25,25);
  ellipse(50, 130, 25, 25);
 }
 
 if(int(cubeScore) == 3){
   fill(135, 0, 255);
 ellipse(150, 35, 25,25);
  ellipse(50, 130, 25, 25);
   ellipse(100,85,25,25);
 }
 
 if(int(cubeScore) == 4){
   fill(135, 0, 255);
 ellipse(150, 35, 25,25);
  ellipse(50, 35, 25, 25);
   ellipse(150, 130, 25,25);
    ellipse(50, 130, 25, 25);
 }
 
 if(int(cubeScore) == 5){
   fill(135, 0, 255);
 ellipse(150, 35, 25,25);
  ellipse(50, 35, 25, 25);
    ellipse(150, 130, 25,25);
     ellipse(50, 130, 25, 25);
      ellipse(100, 85, 25,25);
 }
 
 if(int(cubeScore) == 6){
   fill(135, 0, 255);
  ellipse(65, 40, 25,25);
   ellipse(65, 80, 25,25);
    ellipse(65, 120, 25,25);
     ellipse(135, 40, 25,25);
      ellipse(135, 80, 25,25);
       ellipse(135, 120, 25,25);
}

 }

void mousePressed(){
  
  if(mouseX > ButtonX && mouseX < ButtonX + ButtonW && mouseY > ButtonY && mouseY < ButtonY + ButtonH ){  
    swap = !swap;
   cubeScore = random(1,7);
   
   if (swap == false){
    player1Score += cubeScore;
   }
   
   if (swap == true){
     player2Score += cubeScore;
   }
  
  println(int(cubeScore));
  
  if(swap == false){
  println("Player1Score: " + player1Score);
  }
  
  if(swap == true){
  println("Player2Score: " + player2Score);
  }
 }
}
