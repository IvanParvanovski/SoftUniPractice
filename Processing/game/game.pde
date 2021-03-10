int rectX = 0;
int rectY = 325;
int rectX2 = 765;
int rectY2 = 325;


void setup(){
size(800,800);
}




void draw(){
background(255);
  strokeWeight(10);
  fill(255);
  rect(rectX, rectY, 30,150,9);
  rectX = constrain(rectX,0,650);
  rectY = constrain(rectY,0,650);
  
    rect(rectX2, rectY2, 30,150,9);
  rectX = constrain(rectX,0,650);
  rectY = constrain(rectY,0,650);





 if (keyCode == DOWN){
    rectY += 5;
  }
  
  if (keyCode == UP){
    rectY -= 5;
  } 
  
  if (keyCode == 'W'){
    rectY2 -= 5;
  }
  
  if (keyCode == 'S'){
    rectY2 += 5;
  } 
}
