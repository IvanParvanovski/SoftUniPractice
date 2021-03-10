float total = 100;
int player1 = 0;
int player2 = 0;

boolean swap = false;

void setup(){
size(500,500);
}

void draw (){

}

void mousePressed(){
int randomNumber = int(random(1,20));

 if (swap == false && player2 < 100){
  player1 += randomNumber;
   println("Player1: " + player1);
    swap = !swap;
     
 if (player1 >= total){
  println("Player1 is winner with " + player1 + " points.");
   background(0,255,0);
    
  }
  
 } else if (swap == true && player1 < 100){
    player2 += randomNumber;
     println("Player2: " + player2);
      swap = !swap;
     
  if (player2 >= total){
   println("Player2 wins with" + player2 + " points.");
     
}
}

}
